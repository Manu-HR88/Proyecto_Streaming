# Proyecto_Streaming
*José Manuel Hernández Rojas*

 <br>

Aquí encontrarás un [video explicativo](http:video) que resume el trabajo realizado.

<br>

## Contexto

Para este proyecto se presentó un escenario en donde los servicios de quien suscribe fueron solicitados por una start-up que provee servicios de agregación de plataformas de streaming. Es un trabajo que contempla la recolección, análisis, transformación y modelación de datos, de cero hasta la conformación del modelo de predicción.

## Objetivos

Este proyecto tiene dos objetivos principales. 

* El primero, presentar una API que se pueda consultar y que se pueda obtener información a partir de cuatro funciones.

* El segundo, presentar un sistema de recomendación de películas a partir de el id del usuario.

<br>

## Organización relevante de archivos y carpetas

* 1 API_Streaming *(Contiene la información del ETL):*
    * Datasets - carpeta con los archivos recibidos para trabajar.
    * Funciones FastApi - notebook con las funciones que arrojarán la información de la API.
    * Proceso ETL - notebook con la descripción del trabajo de tranformación realizado.

* 2 Recomendación *(Contiene los archivos para el EDA):*
    * Datasets - carpeta con los archivos procesados para trabajar.
    * Predicción - Contiene la función para predecir la recomendación.
    * Proceso ML - notebook con el EDA y el diseño del modelo.
    * requirements - Archivo txt con las librerías a utilizar en gradio.

* 3 API_Creation  *(Contiene la documentación para el funcionamiento de la API).*


<br>

## Notas a considerar para el funcionamiento

### API_Streaming
Esta API fue creada en Deta Space, por lo que es necesario crear una cuenta y registrarse.

Una vez creada la cuenta, se puede acceder a la API que tiene como nombre [JMHR_Movies_API](https://deta.space/discovery/r/wemu1srh9dzjnspr).

Tiene 7 funciones que son:

1. **Bienvenida**: "/" - aparece al inicio de forma automática.
2. **Menu**: "/menu" - muestra las 4 funciones principales.
3. **Documentación**: "/docs"  - muestra graficamente las 4 funciones principales.
4. **get_max_duration** - muestra la película con mayor duración con filtros opcionales de año, plataforma, tipo de duración.
5. **get_score_count** - muestra la cantidad de películas por plataforma con un puntaje mayor a X en determinado año.
6. **get_count_platform** - muestra la cantidad de películas por plataforma con filtro de plataforma.
7. **get_actor** - muestra al actor que más se repite según plataforma y año.

Para utilizar los filtros es importante tomar en cuenta que se deben colocar en **minúsculas** y son aceptables los siguientes valores:
* Para Year colocaremos: 
    * Un número entre 1920 y 2021 que es el catálogo con el que se cuenta.
    * Un 0 para considerar todos los años.
* Para plataforma colocaremos:
    * amazon - para seleccionar solo las películas de Amazon Prime Video.
    * hulu - para seleccionar solo las películas de Hulu.
    * disney - para seleccionar solo las películas de Disney.
    * netflix - para seleccionar solo las películas de Netflix.
    * none - para seleccionar las cuatro anteriores.
* Para tipo de duración:
    * minutos - para películas.
    * temporadas - para series.
    * none - tanto para películas como series.


Aquí hay algunos ejemplos:
* [get_max_duration/2010/disney/minutos](https://jmhr_movies_api-2-d1140410.deta.app/get_max_duration/2010/disney/minutos)
* [get_score_count/none/3.2/2000](https://jmhr_movies_api-2-d1140410.deta.app/get_score_count/none/3.2/2000)    
* [get_count_platform/amazon](https://jmhr_movies_api-2-d1140410.deta.app/get_count_platform/amazon)
* [get_actor/netflix/1999](https://jmhr_movies_api-2-d1140410.deta.app/get_actor/netflix/1999)

<br>

### Aplicación de Recomendación

Para la aplicación que recomienda los titulos a partir de un id de usuario hay que tener en cuenta lo siguiente:

* Está hecha en la plataforma de gradio, y alojada en "Hugging Face" con el nombre [Peliculas_Recomendación](https://huggingface.co/spaces/ManuHR88/Peliculas_recomendacion).
* Esta interfaz es más gráfica e intuitiva.
* Se ingresa el numero de usuario y un id de la pelicula, el cual puedes corroborar en el archivo llamado "titulos".
* La información sobre el modelo de machine learning lo puedes encontrar en el archivo "Proceso_ML".

<br>

## Nota:

Muchas gracias por llegar hasta aquí y dedicar tu tiempo a revisar este proyecto.

Contacto: manuel.hernandez.rojas@gmail.com

