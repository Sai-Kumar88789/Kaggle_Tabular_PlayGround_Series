from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

with open('kaggle_Playground.pkl', 'rb') as f:
    model = pickle.load(f)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        
        country=request.form['country']
        if(country=='France'):
                country_Germany= 0
                country_France = 1
                country_Italy = 0
                country_poland = 0
                country_spain = 0
        elif(country == 'Germany'):
            country_Germany= 1
            country_France = 0
            country_Italy = 0
            country_poland = 0
            country_spain = 0
        elif(country == 'Italy'):
            country_Germany= 0
            country_France = 0
            country_Italy = 1
            country_poland = 0
            country_spain = 0
        elif(country == 'Poland'):
            country_Germany= 0
            country_France = 0
            country_Italy = 0
            country_poland = 1
            country_spain = 0
        elif(country == 'Spain'):
            country_Germany= 0
            country_France = 0
            country_Italy = 0
            country_poland = 0
            country_spain = 1
        elif(country == 'Belgium'):
            country_Germany= 0
            country_France = 0
            country_Italy = 0
            country_poland = 0
            country_spain = 0

        store=request.form['store']
        if(store=='KaggleRama'):
            store_KaggRama=1
        else:
            store_KaggRama=0
        product =request.form['product']
        if(product=='KaggleGettingStarted'):
            product_KGS = 1
            product_KRB = 0
            product_KFK = 0
        elif(product == 'KaggleRecipeBook'):
            product_KGS = 0
            product_KRB = 1
            product_KFK = 0
        elif(product == 'KaggleforKids'):
            product_KGS = 0
            product_KRB = 0
            product_KFK = 1
        else:
            product_KGS = 0
            product_KRB = 0
            product_KFK = 0

        prediction=model.predict([[country_France,country_Germany,country_Italy,country_poland,country_spain,
            store_KaggRama,product_KGS,product_KRB,product_KFK,year,month,day]])
        output=prediction[0]
      
        return render_template('index.html',prediction_text="the calculated num_sold is  {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

