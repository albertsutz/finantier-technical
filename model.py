import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder

finantier_data_path = "finantier_data_technical_test_dataset.csv"
data = pd.read_csv(finantier_data_path, header=None, sep='\n')
data = data[0].str.split(",", expand=True)
data.columns = data.iloc[0]
data.drop([0], axis =0, inplace=True)
data.reset_index(drop=True)
data.drop(data.columns[[-1,]], axis=1, inplace=True)

column_names = list(data.columns)
column_names.remove('customerID')
column_names.remove('Default')
for i in column_names:
    data = data[(data[i] != "") & (data[i] != " ")]

data["MonthlyCharges"] = pd.to_numeric(data["MonthlyCharges"])
data["tenure"] = pd.to_numeric(data["tenure"])
data["TotalCharges"] = pd.to_numeric(data["TotalCharges"])

y = data["Default"]
y = (y == "Yes") * 1
data.drop(["Default", "customerID"], axis=1, inplace=True)
X = data

numeric_cols = [cname for cname in X.columns if X[cname].dtype in ['int64', 'float64']]
object_cols = [cname for cname in X.columns if X[cname].dtype == "object"]

OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

OH_X = pd.DataFrame(OH_encoder.fit_transform(X[object_cols]))
OH_X.index = X[object_cols].index

num_X = X[numeric_cols]

OH_X= pd.concat([num_X, OH_X], axis=1)

my_model_1 = xgb.XGBRegressor(random_state=0)
my_model_1.fit(OH_X, y)

import joblib
joblib.dump(my_model_1, 'deploy/model.pkl')
print("Model dumped!")

joblib.dump(OH_encoder, "deploy/encoder")
print("encoder dumped!")