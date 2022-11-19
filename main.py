from flask import Flask, render_template

app = Flask (__name__)

@app.route("/", methods=["POST", "GET"])
def portfolio():
    return render_template("portfolio.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html")

@app.route("/sobre-mim", methods=["POST", "GET"])
def sobre_mim():
    return render_template("sobre-mim.html")

@app.route("/projetos", methods=["POST", "GET"])
def projetos():
    return render_template("projetos.html")

@app.route("/redes-sociais", methods=["POST", "GET"])
def redes_sociais():
    return render_template("redes-sociais.html")
    
if __name__ == "__main__":
    app.run(debug=True)