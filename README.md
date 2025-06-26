# PlayStore-Big-Data
## Las Apps más populares

Este proyecto tiene como objetivo explorar y analizar un extenso conjunto de datos sobre aplicaciones de la Google Play Store para identificar patrones y obtener información valiosa sobre el mercado de aplicaciones móviles. Utilizando un dataset con más de 2 millones de registros, se analizarán las categorías más populares, las aplicaciones con más descargas, así como las características clave que influyen en la popularidad y éxito de las apps.

A través de este análisis, buscaremos responder preguntas como:

- ¿Cuáles son las categorías de aplicaciones más populares en la Play Store?

- ¿Qué tipo de aplicaciones de pago obtienen más descargas?

- ¿Qué correlación existe entre las calificaciones de las aplicaciones de pago y su cantidad de descargas?

El dataset incluye información clave sobre cada aplicación, como su nombre, categoría, calificación promedio, número de instalaciones, precio, tamaño y otros atributos, lo que permite realizar un análisis profundo y detallado de las tendencias en la Play Store.

Con este estudio, se pretende obtener una comprensión más clara del panorama actual de las aplicaciones móviles, proporcionando datos valiosos para desarrolladores, empresas y analistas interesados en el mercado de aplicaciones móviles.

## Datos Utilizados 
Usaremos un dataset de la Play Store https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps

Este dataset que contiene un único archivo .csv, y en términos generales contiene datos sobre el rating, categoría, precio, tamaño, etc. 
El dataset cuenta con +2 millones de filas a disposición.

### 📊 Estructura de las Columnas del CSV

El conjunto de datos contiene las siguientes columnas:

-   **App Name**: Nombre de la aplicación

-   **App Id**: Identificador único de la aplicación en la tienda

-   **Category**: Categoría en la que está clasificada la aplicación

-   **Rating**: Calificación promedio dada por los usuarios

-   **Rating Count**: Número total de calificaciones recibidas

-   **Installs**: Número aproximado de instalaciones

-   **Minimum Installs**: Número mínimo de instalaciones reportadas

-   **Maximum Installs**: Número máximo de instalaciones reportadas

-   **Free**: Indica si la aplicación es gratuita (True/False)

-   **Price**: Precio de la aplicación (si no es gratuita)

-   **Currency**: Moneda en la que se muestra el precio

-   **Size**: Tamaño de la aplicación (por ejemplo, MB, KB)

-   **Minimum Android**: Versión mínima de Android requerida para instalar la aplicación

-   **Developer Id**: Identificador único del desarrollador de la aplicación

-   **Developer Website**: Sitio web del desarrollador

-   **Developer Email**: Correo electrónico de contacto del desarrollador

-   **Released**: Fecha de lanzamiento inicial de la aplicación

-  **Last Updated**: Fecha de la última actualización de la aplicación

-   **Content Rating**: Clasificación de contenido o edad recomendada para la aplicación

-   **Privacy Policy**: Enlace a la política de privacidad de la aplicación

-   **Ad Supported**: Indica si la aplicación tiene anuncios (True/False)

-   **In App Purchases**: Indica si la aplicación tiene compras dentro de la app (True/False)

-   **Editors Choice**: Indica si la aplicación ha sido marcada como "Elección del Editor" (True/False)

-   **Scraped Time**: Fecha y hora en que se extrajo la información del conjunto de datos

## Tecnología a utilizar
Este proyecto hace uso de tecnologías de Big Data como Apache Spark para procesar grandes volúmenes de datos, permitiendo análisis rápidos y eficientes en un conjunto de datos tan amplio.

![ApacheSpark](image-1.png)

