import analyze as ppcd
import pandas as pd

# get the vehicle data from the preProcessing file
print(ppcd.vehicle_data.head())

vehicle_data = ppcd.vehicle_data

def set_brand(name):
    if name == 'Honda' or name == 'Toyota' or name == 'BMW' or name == 'Suzuki' or name == 'Mitsubishi':
        return name
    else:
        return 'Other'

vehicle_data['Brand'] = vehicle_data['Brand'].apply(set_brand)


def set_model(name):
    if name == 'Vezel' or name == 'CHR' or name == 'Land Cruiser Prado' or name == 'CRV' or name == 'Vitz' or name == 'Alto' or name == 'Montero' or name == 'Allion':
        return name
    else:
        return 'Other'

vehicle_data['Model'] = vehicle_data['Model'].apply(set_model)

def set_Body(name):
    if name == 'Saloon' or name == 'Hatchback':
        return name
    else:
        return 'Other'

vehicle_data['Body'] = vehicle_data['Body'].apply(set_Body)
print(vehicle_data.head())
vehicle_data = vehicle_data.dropna()