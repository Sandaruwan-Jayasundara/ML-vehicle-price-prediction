from distutils.log import debug
from flask import Flask, render_template, request
import pickle
import numpy as np

app=Flask(__name__)

def prediction(lst):
    filename = 'model/CarPricePredictionModel.pickle'
    with open(filename, 'rb') as file:
        trained_model = pickle.load(file)
    pred_value = trained_model.predict([lst])
    return pred_value


@app.route('/', methods=['POST', 'GET'])
def index():
    value = 0
    if request.method == 'POST':
        brand = request.form['Brand']
        model = request.form['Model']
        year = request.form['Year']
        capacity = request.form['Capacity']
        transmission = request.form['Transmission']
        condition = request.form['Condition']
        mileage = request.form['Mileage']
        body = request.form['body']
        fuel = request.form['Fuel']


        list_array = []

        list_array.append(int(year))
        list_array.append(float(capacity))
        list_array.append(float(mileage))

        brand_list = ['BMW', 'Honda', 'Mitsubishi', 'Other', 'Suzuki', 'Toyota']
        model_list = ['Allion', 'Alto', 'CHR', 'CRV', 'Land Cruiser Prado', 'Montero', 'Other', 'Vezel', 'Vitz']
        condition_list = ['New', 'Recondition', 'Reconditioned', 'Used','e']
        transmission_list = ['Automatic', 'Other', 'Saloon', '0', '1000', '11', '1200', '125', '1490', '150', '1500', '175', '2', '200', '2001','205', '444444444','450', '50', '650','Tiptronic']
        body_list = ['Hatchback', 'Other', 'Saloon']
        fuel_list = [ 'CNG','Diesel','Electric','Gas','Hybrid','Kick','Petrol','Other', 'type']

        def selection_list(lst, value):
            for item in lst:
                if item == value:
                    list_array.append(1)
                else:
                    list_array.append(0)

        selection_list(brand_list, brand)
        selection_list(model_list, model)
        selection_list(condition_list, condition)
        selection_list(transmission_list, transmission)
        selection_list(body_list, body)
        selection_list(fuel_list, fuel)

        value = prediction(list_array)



    return render_template('prediction.html', pred_value=value)


if __name__ == '__main__':
    app.run(debug=True)
