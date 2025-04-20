from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'app': 'Mi Aplicación Flask',
        'version': '1.0',
        'autor': 'Jazelis Marrero'
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    nombre = data.get('nombre', 'anónimo')
    return jsonify({
        'respuesta': f'¡Hola, {nombre}! Tu mensaje ha sido recibido.'
    })

if __name__ == '__main__':
    app.run(debug=True)
