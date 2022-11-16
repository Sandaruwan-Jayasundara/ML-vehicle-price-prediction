import process as prc
import pandas as pd

vehicle_data = prc.vehicle_data

vehicle_data=pd.get_dummies(vehicle_data)

print(vehicle_data.head(10))
print(vehicle_data.shape)

x= vehicle_data.drop('Price', axis=1)
y= vehicle_data['Price']

from sklearn.model_selection import train_test_split
x_train_axis, X_test_axis, y_train_axis, y_test_axis = train_test_split(x, y, test_size=0.25)

print(x_train_axis.shape, X_test_axis.shape)

def model_accuracy(model):
    model.fit(x_train_axis,y_train_axis)
    accuracy = model.score(X_test_axis,y_test_axis)
    print(str(model)+'=>'+str(accuracy))

from sklearn.linear_model import LinearRegression
LinearReg=LinearRegression()
model_accuracy(LinearReg)

from sklearn.tree import DecisionTreeRegressor
DecisionTree=DecisionTreeRegressor()
model_accuracy(DecisionTree)

from sklearn.ensemble import RandomForestRegressor
RandomForest=RandomForestRegressor()
model_accuracy(RandomForest)

from sklearn.model_selection import GridSearchCV

Parameters = {'n_estimators':[10, 50, 100],
                 'criterion':['squared_error','absolute_error','poisson']}
grid_obj = GridSearchCV(estimator=RandomForest, param_grid=Parameters)
grid_fit=grid_obj.fit(x_train_axis, y_train_axis)

best_model = grid_fit.best_estimator_
print(best_model)

score_value=best_model.score(X_test_axis,y_test_axis)
print(score_value)

import pickle
with open('VehiclePricePredictionModel.pickle', 'wb') as file:
    pickle.dump(best_model, file)