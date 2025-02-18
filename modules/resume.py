globalJSONFilePath = 'data/finances.json'

def showBalance():
    from modules.revenue import loadData
    data = loadData(globalJSONFilePath)
    return sum(item["value"] for item in data['revenues'])

def showAll():
   from modules.revenue import loadData
   data = loadData(globalJSONFilePath)
   return data.get('revenues', [])

def getSummary():
    from modules.revenue import loadData
    data = loadData(globalJSONFilePath)
    total = len(data['revenues'])
    revenues = {r['name'] for r in data['revenues']}
    categorias = {r["category"] for r in data['revenues']}

    return [
        f"Total de receitas: {total}",
        f"Receitas: {revenues}",
        f"Categorias únicas: {len(categorias)}",
        f"Categorias: {categorias}"
    ]             