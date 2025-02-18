globalJSONFilePath = 'data/data.json'

def showBalance():
    from modules.revenue import loadData
    data = loadData(globalJSONFilePath)
    actualBalance = 0.0
    for args in data:
        actualBalance += args['value']
    print(f'Actual Balance: {actualBalance}')

def showPositiveRevenues():
    from modules.revenue import loadData
    data = loadData(globalJSONFilePath)

    for args in data:
        if args['value'] > 0:
            print(f'Nome: {args['name']} | Valor: {args['value']}')

def showNegativeRevenues():
    from modules.revenue import loadData
    data = loadData(globalJSONFilePath)

    for args in data:
        if args['value'] < 0:
            print(f'Nome: {args['name']} | Valor: {args['value']}')

def showAll():
   from modules.revenue import loadData
   data = loadData(globalJSONFilePath)

   for args in data:
       print(f'Nome: {args['name']} | Data: {args['date']} | Valor: {args['value']}')       