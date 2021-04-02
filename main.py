from regression_model import train_model, predict
from sanic import Sanic, response as res
#from sklearn.preprocessing import OrdinalEncoder
from regression_model import OrdinalEncoder
from regression_model import enc

enc = OrdinalEncoder() 

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
  prediction = predict([enc.transform([[values['artists']]]).ravel(), values['acousticness'],values['year']])

  # send prediction as json
  return res.json(prediction.tolist())

# start webserver
if __name__ == '__main__':
  app.run(port=8000)