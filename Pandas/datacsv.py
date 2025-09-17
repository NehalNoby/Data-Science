from sklearn.impute import KNNImputer
import pandas as pd
data = pd.read_csv("Pandas\MISSING_DATASET_HANDLING.csv",encoding='latin1')
# data=data.drop(columns=["ADDRESSLINE2"])
# data=data.dropna(subset=["ORDERDATE","PRODUCTLINE"])
# data["MSRP"]=data["MSRP"].fillna(data["MSRP"].median())
# data["YEAR_ID"]=data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0])
# data["STATUS"].fillna(data["STATUS"].mode()[0],inplace=True)
# data["PHONE"].fillna("Unknown",inplace=True)
print(data.isnull().sum())
imputer=KNNImputer(n_neighbors=5)
data_imputed=pd.DataFrame(imputer.fit_transform(data.select_dtypes(include=['float','int'])),columns=data.select_dtypes(include=['float','int']).columns)
print(data_imputed.isnull().sum())