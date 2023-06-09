# Datos Externos

La mayoría de los datos en la carpeta "external" son de fuentes públicas, como el portal de Datos Abiertos de Bogotá ([https://datosabiertos.bogota.gov.co/](https://datosabiertos.bogota.gov.co/)). Estos datos se proporcionan de manera gratuita y abierta por parte del gobierno de Bogotá para su uso público. Asegúrate de revisar y cumplir con los términos y condiciones de uso de cada fuente de datos antes de utilizarlos.

Es importante mencionar que estos datos son proporcionados "tal cual" y no se garantiza su precisión o integridad. Si planeas utilizar estos datos en tu propio proyecto, te recomendamos verificar su calidad y realizar cualquier procesamiento o limpieza adicional según sea necesario.

### Files:

- `barrios_bogota/` - Listado de todos los barrios de Bogotá junto con su ubicación geográfica. Período de vigencia: 2016. 
**_link:_** [https://bogota-laburbano.opendatasoft.com/explore/dataset/barrios_prueba/information/?flg=es](https://bogota-laburbano.opendatasoft.com/explore/dataset/barrios_prueba/information/?flg=es)

- `estaciones_troncales_transmilenio/` - Son los puntos de parada sobre los corredores troncales en los que existe integración física entre rutas troncales y los usuarios para acceder al servicio, trasbordar o salir del Sistema Transmilenio. **_link:_** [https://datosabiertos-transmilenio.hub.arcgis.com/datasets/Transmilenio::estaciones-troncales-de-transmilenio/explore](https://datosabiertos-transmilenio.hub.arcgis.com/datasets/Transmilenio::estaciones-troncales-de-transmilenio/explore)

    **_API_**: [https://gis.transmilenio.gov.co/arcgis/rest/services/Troncal/consulta_estaciones_troncales/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson](https://gis.transmilenio.gov.co/arcgis/rest/services/Troncal/consulta_estaciones_troncales/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson)

    **Fuente: TRANSMILENIO S.A: www.transmilenio.gov.co**

- `localidades_bogota/` - División política, administrativa y territorial municipal, con competencias claras y criterios de financiación y aplicación de recursos, creada por el Concejo Municipal a iniciativa del alcalde respectivo, con el fin de atender de manera más eficaz las necesidades de esa porción del territorio. **_link:_** [https://datosabiertos.bogota.gov.co/dataset/localidad-bogota-d-c](https://datosabiertos.bogota.gov.co/dataset/localidad-bogota-d-c)

    **_API_**: [https://datosabiertos.bogota.gov.co/dataset/856cb657-8ca3-4ee8-857f-37211173b1f8/resource/497b8756-0927-4aee-8da9-ca4e32ca3a8a/download/loca.json](https://datosabiertos.bogota.gov.co/dataset/856cb657-8ca3-4ee8-857f-37211173b1f8/resource/497b8756-0927-4aee-8da9-ca4e32ca3a8a/download/loca.json)

- `paraderos_zonales_SITP/` - Son los puntos localizados sobre los corredores de tráfico mixto utilizados para la operación no troncal de los vehículos del SITP. Estos puntos son los únicos autorizados para recoger y dejar pasajeros; éstos podrán tener diferente tratamiento físico dependiendo del corredor y de su demanda. **_link:_** [https://datosabiertos.bogota.gov.co/dataset/paraderos-zonales-del-sitp](https://datosabiertos.bogota.gov.co/dataset/paraderos-zonales-del-sitp)