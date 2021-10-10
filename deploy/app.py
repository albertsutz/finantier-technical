# Dependencies
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict', methods=['POST'])
def predict():
    if lr:
        json_ = request.json
        print(json_)
        query = pd.DataFrame(json_)
        query["MonthlyCharges"] = pd.to_numeric(query["MonthlyCharges"])
        query["tenure"] = pd.to_numeric(query["tenure"])
        query["TotalCharges"] = pd.to_numeric(query["TotalCharges"])
        query.drop(["customerID"], axis=1, inplace=True)

        OH_query = pd.DataFrame(encoder.transform(query[object_cols]))
        OH_query.index = query[object_cols].index
        num_query = query = query[numeric_cols]
        OH_query = pd.concat([num_query, OH_query], axis=1)


        prediction = list(lr.predict(OH_query))
        final = ["Yes" if x >= 0.5 else "No" for x in prediction]
        return jsonify({'prediction': str(final)})
    else:
        print ('Train the model first')
        return ('No model here to use')


if __name__ == '__main__':

    lr = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    encoder = joblib.load("encoder")
    print('Encoder loaded')

    object_cols = ['gender',
                    'SeniorCitizen',
                    'Partner',
                    'Dependents',
                    'PhoneService',
                    'MultipleLines',
                    'InternetService',
                    'OnlineSecurity',
                    'OnlineBackup',
                    'DeviceProtection',
                    'TechSupport',
                    'StreamingTV',
                    'StreamingMovies',
                    'Contract',
                    'PaperlessBilling',
                    'PaymentMethod']
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    app.run(host='0.0.0.0', port='3000')