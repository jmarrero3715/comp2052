from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de usuarios simulando almacenamiento en memoria
usuarios = []

# Ruta GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "app": "Gestión de Usuarios",
        "versión": "1.0",
        "autor": "Jazelis Marrero",
        "endpoints": ["/info", "/crear_usuario", "/usuarios"]
    }), 200

# Ruta POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos JSON"}), 400

    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Faltan campos requeridos: 'nombre' y 'correo'"}), 400

    usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(usuario)

    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": usuario}), 201

# Ruta GET /usuarios
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify({"usuarios": usuarios}), 200

if __name__ == "__main__":
    app.run(debug=True)
