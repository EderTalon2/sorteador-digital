from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        itens = request.form.get("itens")

        if itens:
            lista = [item.strip() for item in itens.split(",") if item.strip()]

            if lista:
                resultado = random.choice(lista)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
