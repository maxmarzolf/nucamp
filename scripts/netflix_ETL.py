import pandas
from sqlalchemy import create_engine
from sqlalchemy.types import String, Date, Float


engine = create_engine('postgresql://postgres:@localhost:5432/netflix')
column_names = ['title', 'genre', 'premiere', 'runtime', 'imdb_score', 'language']
df = pandas.read_csv('NetflixOriginals.csv', encoding="ISO-8859-1", names=column_names, index_col=0)
df = df.iloc[1:]

df.to_sql('netflix_originals', engine, dtype={'title': String, 'genre': String, 'premiere': Date, 'runtime': Float,
                                              'imdb_score': Float, 'language': String})