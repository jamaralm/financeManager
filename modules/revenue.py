import json
from datetime import date

globalJSONFilePath = 'data/data.json'

def loadData(filePath):
    try:
        with open(filePath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print('JSON DECODE ERROR')
    except FileNotFoundError:
        print('FILE NOT FOUND!')

def saveData(data):
    with open(globalJSONFilePath, 'w') as file:
        json.dump(data, file, indent=4)

def transformInputToJSON(name,value, date,category):
    inputObject = {
        'name': name,
        'value': value,
        'date': date,
        'category': category
    }
    return inputObject

def addRevenue(name, value, date, category):
    data = loadData(globalJSONFilePath)
    revenue = transformInputToJSON(name, value, date, category)
    data.append(revenue)
    saveData(data)