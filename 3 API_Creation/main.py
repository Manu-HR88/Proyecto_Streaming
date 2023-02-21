from fastapi import FastAPI
import pandas as pd
from deta import Deta
from io import StringIO 

app = FastAPI()


#films = pd.read_csv('films.csv')

@app.get("/")
def index():
    return {"Bienvenido": "a esta API para hacer consultas sobre plataformas de streaming"}

@app.get("/menu")
def mostrar_menu():
    return {"Las funciones de esta API son":"1.get_max_duration | 2)get_score_count | 3)get_count_platform | 4)get_actor"}


# La clase Peliculas y las funciones que se utilizarán se encuentran descritas de forma específica en el archivo "Funciones"

# Definimos la clase Peliculas que nos va a realizar los filtros de año, plataforma, duración.

class Peliculas:
    
    def __init__(self,df):
        self.df = df

    def year_filter(self,year):
        self.year = year
        if self.year < 1920:
            return ('No contamos con películas anteriores a 1920.')
        elif self.year > 2021:
            return ('No contamos con películas posteriores a 2021.')
        else:
            return self.df[self.df['release_year']==self.year]
    
    def platform_filter(self,platform):
        self.platform = platform
        if self.platform=='amazon' or self.platform=='disney' or self.platform=='hulu' or self.platform=='netflix':
            return self.df[self.df['platform']==self.platform]
        else:
            return ("Revisa que hayas escrito de manera correcta la plataforma solicitada. Las opciones son: 'amazon', 'disney', 'hulu', 'netflix'")
        
    def duration_filter(self,duration):
        self.duration = duration
        if self.duration == 'minutos': 
            self.duration = 'min'    
        elif self.duration=='temporadas':
            self.duration = 'season'
        else:
            return ("No se ha seleccionado un criterio de tiempo adecuado. Las opciones son: 'minutos' o 'temporadas")
        return self.df[self.df['duration_type']==self.duration]



# 1 Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN

@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
def get_max_duration(year:int, platform:str, duration_type:str):
    films = pd.read_csv('films.csv')
    if year == 0:
        filtroanio = films
    else:
        filtroanio = Peliculas(films)
        filtroanio = filtroanio.year_filter(year)
        if type(filtroanio) == str: return filtroanio
    
    if platform == 'none':
        filtroplat = filtroanio
    else:
        filtroplat = Peliculas(filtroanio)
        filtroplat = filtroplat.platform_filter(platform)
        if type(filtroplat) == str: return filtroplat 

    if duration_type == 'none':
        filtroduration = filtroplat
    else:
        filtroduration = Peliculas(filtroplat) #Intanciamos el df para aplicarle el filtro
        filtroduration = filtroduration.duration_filter(duration_type)
        if type(filtroduration) == str: return filtroduration

    duration_max = filtroduration['duration_int'].max()
    title_movie = filtroduration.loc[filtroduration['duration_int']==duration_max, 'title'].iloc[0]    
    return {"El titulo con mayor duración es": title_movie}


# 2 Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform:str, scored:float, year:int):
    films = pd.read_csv('films.csv')
    if platform == 'none':
        filtroplat = films
    else:
        filtroplat = Peliculas(films)
        filtroplat = filtroplat.platform_filter(platform)
        if type(filtroplat) == str: return filtroplat

    if year == 0:
        filtroanio = filtroplat
    else:
        filtroanio = Peliculas(filtroplat)
        filtroanio = filtroanio.year_filter(year)
        if type(filtroanio) == str: return filtroanio
    
    puntuacion = filtroanio[filtroanio["rating"]>scored]
    num_movies = puntuacion.shape[0]

    return {f"Cantidad de peliculas con puntaje mayor a {scored}": num_movies}


# 3 Cantidad de películas por plataforma con filtro de PLATAFORMA.

@app.get("/get_count_platform/{platform}")
def get_count_platform(platform:str):
    films = pd.read_csv('films.csv')
    if platform == 'none':
        filtroplat = films
    else:
        filtroplat = Peliculas(films)
        filtroplat = filtroplat.platform_filter(platform)
        if type(filtroplat) == str: return filtroplat

    
    movies = filtroplat.shape[0]

    return {"Cantidad de películas": movies}

# 4 Actor que más se repite según plataforma y año.

@app.get("/get_actor/{platform}/{year}")
def get_actor(platform:str, year:int):
    films = pd.read_csv('films.csv')
    if platform == 'none':
        filtroplat = films
    else:
        filtroplat = Peliculas(films)
        filtroplat = filtroplat.platform_filter(platform)
        if type(filtroplat) == str: return filtroplat

    if year == 0:
        filtroanio = filtroplat
    else:
        filtroanio = Peliculas(filtroplat)
        filtroanio = filtroanio.year_filter(year)
        if type(filtroanio) == str: return filtroanio

    df_actors = filtroanio['cast'].str.split(',') 
    apariciones = df_actors.explode().value_counts()
    actor_max_apar = apariciones.idxmax()
    return {'El actor que más aparece es':actor_max_apar}