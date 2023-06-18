from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium import webdriver
from datetime import datetime
import json
import time

# Scrapy
from bogota_apartments.items import ApartmenstItem
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
import scrapy


class MetrocuadradoSpider(scrapy.Spider):
    name = 'metrocuadrado'
    allowed_domains = ['metrocuadrado.com']
    base_url = 'https://www.metrocuadrado.com/rest-search/search'

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920x1080')
        chrome_options.add_argument(f'user-agent={UserAgent().random}')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def start_requests(self):
        headers = {
            'X-Api-Key': 'P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl',
            'User-Agent': UserAgent().random
        }

        for type in ['venta', 'arriendo']:
            for offset in range(0, 150, 50):
                url = f'{self.base_url}?realEstateTypeList=apartamento&realEstateBusinessList={type}&city=bogot%C3%A1&from={offset}&size=50'

                yield scrapy.Request(url, headers=headers, callback=self.parse)

        
    def parse(self, response,):
        result = json.loads(response.body)['results']

        for item in result:
            yield scrapy.Request(
                url=f'https://metrocuadrado.com{item["link"]}',
                callback=self.details_parse
            )

    def details_parse(self, response):
        self.driver.get(response.url)   

        script_data = Selector(text=self.driver.page_source).xpath(
            '//script[@id="__NEXT_DATA__"]/text()'
        ).get()

        script_data = json.loads(script_data)['props']['initialProps']['pageProps']['realEstate']

        for item in script_data:
            loader = ItemLoader(item=ApartmenstItem(), selector=item)
            loader.add_value('codigo', script_data['propertyId'])
            loader.add_value('tipo_propiedad', script_data['propertyType']['nombre'])
            loader.add_value('tipo_operacion', script_data['businessType'])
            loader.add_value('precio_venta', script_data['salePrice'])
            loader.add_value('precio_arriendo', script_data['rentPrice'])
            loader.add_value('area', script_data['area'])
            loader.add_value('habitaciones', script_data['rooms'])
            loader.add_value('banos', script_data['bathrooms'])
            loader.add_value('administracion', script_data['detail']['adminPrice'])
            loader.add_value('parqueaderos', script_data['garages'])
            loader.add_value('sector', script_data['sector']['nombre'])
            loader.add_value('estrato', script_data['stratum'])
            loader.add_value('antiguedad', script_data['builtTime'])
            loader.add_value('estado', script_data['propertyState'])
            loader.add_value('longitud', script_data['coordinates']['lon'])
            loader.add_value('latitud', script_data['coordinates']['lat'])
            loader.add_value('featured_interior', script_data['featured'][0]['items'])
            loader.add_value('featured_exterior', script_data['featured'][1]['items'])
            try:
                loader.add_value('featured_zona_comun', script_data['featured'][2]['items'])
            except:
                pass
            try:
                loader.add_value('featured_sector', script_data['featured'][3]['items'])
            except:
                pass
            loader.add_value('descripcion', script_data['comment'])
            loader.add_value('datetime', datetime.now())

        yield loader.load_item()

    def close(self, spider):
        self.driver.quit()

