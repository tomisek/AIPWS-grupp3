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

  # get prediction with provided values
  # if values['artists'] == df['artists']:
  #   print("Yes, 'apple' is in the fruits list")

  artistic = "[" + "'" + values['artists'] + "'" + "]"
  print(values['artists'])

  prediction = predict([enc.transform([[artistic]]).ravel()[0], values['acousticness'],values['year']])

  return res.json(prediction.tolist())

# start webserver
if __name__ == '__main__':
  app.run(port=8000)