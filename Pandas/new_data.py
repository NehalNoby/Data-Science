import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset: house size (X) → house price (y)
X = np.array([500, 800, 1000, 1200, 1500]).reshape(-1,1)  # sqft
y = np.array([150000, 200000, 230000, 260000, 300000]) # price in $
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict([[100]])
print("Predictions:", y_pred)



