from regression_model import train_model, predict
from sanic import Sanic, response as res
#from sklearn.preprocessing import OrdinalEncoder
from regression_model import OrdinalEncoder
from regression_model import enc
import sqlite3
import numpy as np


app = Sanic(__name__)

train_model()

@app.get('/api/genres')
async def get_all_genres(req):
  from database import get_genres
  return res.json(await get_genres())

@app.post('/api/predict')
async def predict_click(req):
  values = req.json

  # artistic = "[" + "'" + values['artists'] + "'" + "]"
  values['artists'] = "[" + "'" + values['artists'] + "'" + "]"
  # get prediction with provided values
  prediction = predict([enc.transform([[values['artists']]]).ravel()[0],values['acousticness'],values['danceability'],values['energy'],values['explicit'],values['instrumentalness'],values['key'],values['liveness'],values['speechiness'],values['valence'],values['year'],values['tempo'],values['loudness'],values['duration_ms'],values['release_date_month'],values['release_date_day'],values['release_date_dayofweek']])
  print(prediction)
  # artistical = enc.transform([[artistic]]).ravel()[0]
  # print(values['artists'])
  # print(artistical)
  # print(artistic)

  acou = values['acousticness']
  art = values['artists']
  dance = values['danceability']
  dura = values['duration_ms']
  ener = values['energy'] 
  expli = values['explicit']
  ids =  'default'
  instrument = values['instrumentalness']
  key = values['key']
  liveness = values['liveness'] 
  loudness = values['loudness']
  mode = 0
  name = 'default'
  popularity = float(prediction)
  release_date = str(values['year']) + "-" + str(values['release_date_month']).zfill(2) + "-" + str(values['release_date_day']).zfill(2)
  speech = values['speechiness']
  tempo = values['tempo']
  valence = values['valence']
  year = values['year']

  con = sqlite3.connect('spotify_dataset.db')

  cur = con.cursor()

  cur.execute("INSERT INTO dataset(acousticness, artists, danceability, duration_ms, energy, explicit, id, instrumentalness, key, liveness, loudness, mode, name, popularity, release_date, speechiness, tempo, valence, year) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (acou, art,dance, dura, ener, expli, ids, instrument, key, liveness, loudness, mode, name, popularity, release_date, speech, tempo, valence, year ))
  
  con.commit()

  con.close()

  return res.json(prediction.tolist())

# start webserver
if __name__ == '__main__':
  app.run(port=8000)