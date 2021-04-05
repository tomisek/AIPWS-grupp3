from regression_model import train_model, predict
from sanic import Sanic, response as res
#from sklearn.preprocessing import OrdinalEncoder
from regression_model import OrdinalEncoder
from regression_model import enc


app = Sanic(__name__)

train_model()

# possible ways to call the endpoint
# GET /api/predict/:age/:income
# POST /api/predict
# { age, income }

@app.post('/api/predict')
async def predict_click(req):
  values = req.json

  # artistic = "[" + "'" + values['artists'] + "'" + "]"
  values['artists'] = "[" + "'" + values['artists'] + "'" + "]"
  # get prediction with provided values
  prediction = predict([enc.transform([[values['artists']]]).ravel()[0],values['acousticness'],values['danceability'],values['energy'],values['explicit'],values['instrumentalness'],values['key'],values['liveness'],values['speechiness'],values['valence'],values['year'],values['tempo'],values['loudness'],values['duration_ms'],values['release_date_month'],values['release_date_day'],values['release_date_dayofweek']])

  # artistical = enc.transform([[artistic]]).ravel()[0]
  # print(values['artists'])
  # print(artistical)
  # print(artistic)


  return res.json(prediction.tolist())

# start webserver
if __name__ == '__main__':
  app.run(port=8000)