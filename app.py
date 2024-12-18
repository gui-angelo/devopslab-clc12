from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Guilherme Angelo v2.0 - Lab Concluído"