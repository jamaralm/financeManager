import json
from datetime import date

globalJSONFilePath = 'data/finances.json'

def loadData(filePath):
    try:
        with open(filePath, "r") as file:
            data = json.load(file)
            
            # Se for uma lista, transforma em um dicionário válido
            if isinstance(data, list):
                return {"revenues": data}

            # Se for um dicionário, retorna normalmente
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"revenues": []}

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
    data['revenues'].append(revenue)
    saveData(data)