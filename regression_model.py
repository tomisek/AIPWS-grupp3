import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import xgboost as xgb


from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


#enc = OrdinalEncoder(handle_unknown = 'use_encoded_value', unknown_value = int)
enc = OrdinalEncoder(dtype = 'int64')

xgb_r = xgb.XGBRegressor(
    max_depth=13,
    min_child_weight= 8,
    eta=.05,
    subsample= 0.7,
    colsample_bytree= 0.7,
    objective='reg:squarederror',
    n_estimators=100)


def train_model():
    con = sqlite3.connect('spotify_dataset.db')
    df = pd.read_sql_query('SELECT * FROM dataset', con)

    df['release_date'] = pd.to_datetime(df['release_date'])
    df['release_date_month'] = df['release_date'].dt.month
    df['release_date_day'] = df['release_date'].dt.day
    df['release_date_dayofweek'] = df['release_date'].dt.dayofweek

    df.drop(df[df['loudness'] == -60].index, inplace=True)
    df.drop(df[df['year'] <=1921].index, inplace=True)
    df = df[['artists',
         'acousticness',
         #'danceability',
         #'energy',
         #'explicit',
         #'instrumentalness',
         #'key',
         #'liveness',
         #'mode',
         #'speechiness',
         #'valence',
         'year',
         #'tempo',
         #'loudness',
         #'duration_ms',
         #'release_date',
         #'release_date_month',
         #'release_date_day',
         #'release_date_dayofweek',
         'popularity']]
    
    X= df.iloc[:, :-1].values
    y= df.iloc[:, -1].values

    X[:,0] = enc.fit_transform(X[:,0].reshape(-1,1)).ravel()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)


    xgb_r.fit(X_train, y_train)

    y_pred = xgb_r.predict(X_test)

    print("r2_score:", r2_score(y_test, y_pred))
    print("mse:", mean_squared_error(y_test, y_pred))
    print("rmse:", mean_squared_error(y_test, y_pred, squared=False))

    #df['artists'] = X[:,0]

    con.close()



def predict(predict_values):

    # try: 
    #     artist = enc.transform([["['Madonna']"]]).ravel()[0]
    # except ValueError: 
    #     artist = enc.transform([["['Harry Styles']"]]).ravel()[0]
    # print(artist)

    

    # predict_values = ([enc.transform([["['Uli']"]]).ravel(), 0.678, 1920])
    # print(predict_values)

    probability_of_popularity = xgb_r.predict(np.array(predict_values).reshape((1,-1)))

    return probability_of_popularity