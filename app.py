from flask import Flask, render_template, request, redirect, url_for
from modules.revenue import addRevenue
from modules.resume import showBalance, getSummary, showAll

app = Flask(__name__)

# Função para calcular o saldo e compartilhar com todas as páginas
@app.context_processor
def balance_context():
    return {'balance': showBalance()}

# Rota principal (Adicionar Receita)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        value = float(request.form.get("value"))
        date = request.form.get("date")
        category = request.form.get("category")
        
        addRevenue(name, value, date, category)
        return redirect(url_for("index"))

    return render_template("add_revenue.html")

# Rota para exibir todas as receitas (showAll)
@app.route("/revenues")
def all_revenues():
    revenues = showAll()
    return render_template("all_revenues.html", revenues=revenues)

# Rota para as funções do resumo (resume.py)
@app.route("/summary")
def summary():
    summary_data = getSummary()
    return render_template("summary.html", summary=summary_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
