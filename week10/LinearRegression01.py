# Are there a linear relationship here in this csv data:

# csv
# year,GDP(trillion),4wheeler_car_sale
# 2011,6.2,26.3
# 2012,6.5,26.65
# 2013,5.48,25.03
# 2014,6.54,26.01
# 2015,7.18,27.9
# 2016,7.93,30.47
# save data in a file: car_sales.csv
# plot car sales as a function to GDP (is there a linear relationship?)
# fit data to a klearn linear regression model
# predict sales if GDP hits 9 trillion lakhs

import pandas as pd
import sklearn.linear_model
import numpy as np


df = pd.read_csv("car_sales.csv")

print(df)

xs = df["GDP(trillion)"]
print()
print("xs")
print(xs)
ys = df["4wheeler_car_sale"]
print()
print("ys")
print(ys)

xs_reshape = np.array(xs).reshape(-1, 1)
print()
print("xs_reshape")
print(xs_reshape)
model = sklearn.linear_model.LinearRegression()
print()
print("model")
print(model)
model.fit(xs_reshape, ys)
predicted = model.predict(xs_reshape)
trillion = model.predict([[9]])
print(trillion[0])
