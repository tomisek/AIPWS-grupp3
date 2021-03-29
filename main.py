from regression_model import train_model, predict
from sanic import Sanic, response as res

app = Sanic(__name__)

train_model()

print(predict([6316.0, 0.678, 2020]))

# possible ways to call the endpoint
# GET /api/predict/:age/:income
# POST /api/predict
# { age, income }

@app.post('/api/predict')
async def predict_click(req):
  values = req.json

  # get prediction with provided values
  prediction = predict([values['artists'],values['acousticness'],values['year']])  

  # send prediction as json
  return res.json(prediction.tolist())

# start webserver
if __name__ == '__main__':
  app.run(port=8000)