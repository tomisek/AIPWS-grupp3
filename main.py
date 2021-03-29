from regression_model import train_model, predict
from sanic import Sanic, response as res

train_model()

print(predict([6316.0, 0.678, 0.336, 0.2678, 0, 0.0218, 1, 0.212, 0.3456, 0.397, 1960, 169.980, -27.320, 126903, 4, 5, 5]))


app = Sanic('app')

# possible ways to call the endpoint
# GET /api/predict/:age/:income

# POST /api/predict
# { age, income }

@app.post('/api/predict')
async def predict_click(req):
  predict_values = req.json

  # get prediction with provided values
  prediction = predict(predict_values = ['artists', 'acousticness','danceability','energy','explicit',
         'instrumentalness',
         'key',
         'liveness',
         'speechiness',
         'valence',
         'year',
         'tempo',
         'loudness',
         'duration_ms',
         'release_date_month',
         'release_date_day',
         'release_date_dayofweek'])

  # send prediction as json
  return res.json(prediction)

# start webserver
if __name__ == '__main__':
  app.run(port=6000)