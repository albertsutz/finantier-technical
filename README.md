# finantier-technical
Hi and welcome to this repository. This is a public repository in which I clean and process data to make a machine learning model, which will be used for prediction.
This is my submission for Finantier technical assessment for data scientist/machine learning engineer position
  
My name is **Albert Sutiono**
  
Code that I used for cleaning and creating the model is in **model.py**. After running model.py, it would create **model.pkl** and **encoder** to be used inside the deploy directory. However, to save time, **model.pkl** and **encoder** has been created and stored inside the deploy directory.

## How to run the code
1. Clone the git repository
2. cd finantier-technical && cd deploy
3. docker build -t finantier_assessment:1.0 .
4. Wait until docker finishes building the container
5. docker run -p 5000:3000 finantier_assessment:1.0
6. It is ready to receive

## REST API
**Method: GET**  
Url: http://localhost:5000  
Response: A simple html to check whether the server is running  
  
  
**Method: POST**  
Url: http://localhost:5000/predict  
Body: <insert data in json format>  
Response: A list of "Yes" and "No" to denote the answer  
  
## Body Format for Prediction
```
  [
    {
        "customerID": "7590-VHVEG",
        "gender": "Female",
        "SeniorCitizen": "0",
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": "1",
        "PhoneService": "No",
        "MultipleLines": "No phone service",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": "29.85",
        "TotalCharges": "29.85"
    },
    {
        "customerID": "3668-QPYBK",
        "gender": "Male",
        "SeniorCitizen": "0",
        "Partner": "No",
        "Dependents": "No",
        "tenure": "2",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Mailed check",
        "MonthlyCharges": "53.85",
        "TotalCharges": "108.15"
    }
  ]
```
## Response Format
```
  {
    "prediction": "['No', 'Yes']"
  }
```
