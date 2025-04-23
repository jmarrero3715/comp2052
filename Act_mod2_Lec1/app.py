from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Almacenamiento temporal (memoria)
notas = [
    {"titulo": "Tarea Flask", "contenido": "Terminar la práctica de plantillas"},
    {"titulo": "Recordatorio", "contenido": "Enviar el proyecto el lunes"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/notas")
def ver_notas():
    return render_template("notas.html", notas=notas)

@app.route("/nueva_nota", methods=["GET", "POST"])
def nueva_nota():
    if request.method == "POST":
        titulo = request.form["titulo"]
        contenido = request.form["contenido"]
        notas.append({"titulo": titulo, "contenido": contenido})
        return redirect(url_for("ver_notas"))
    return render_template("nueva_nota.html")

if __name__ == "__main__":
    app.run(debug=True)
