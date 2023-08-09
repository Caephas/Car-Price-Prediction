from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pickle.load(open('regression_car_data.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.htm')


standard_to = StandardScaler()

@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type=0
    if request.method == 'POST':
        Year = int(request.form['number of years'])
        number_of_years = 2023 - Year
        
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Owner=int(request.form['Owner'])
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type== 'Petrol'):
                Fuel_Type= 0
                
        elif(Fuel_Type=='Diesel'):
            Fuel_Type= 1
        elif(Fuel_Type=='CNG'):
            Fuel_Type = 2
            
        Seller_Type=request.form['Seller_Type']
        if(Seller_Type=='Dealer'):
            Seller_Type= 0
        elif(Seller_Type=='Individual'):
            Seller_Type=1
        Transmission=request.form['Transmission']
        if(Transmission=='Manual'):
            Transmission=0
        elif(Transmission=='Automatic'):
            Transmission=1
            
        # prediction = model.predict([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, number_of_years ]])
        # Create a DataFrame with the correct feature names
        input_data = pd.DataFrame([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, number_of_years]],
                              columns=['Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'number of years'])
        prediction = model.predict(input_data)
        
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.htm',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.htm',prediction_text="You Can Sell The Car at {} lakhs".format(output))
    else:
        return render_template('index.htm')
    
if __name__=="__main__":
    app.run(debug=True)


