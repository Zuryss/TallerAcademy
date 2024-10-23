from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    datos = [
        {"id": 1, "nombre": "Elemento 1", "descripcion": "Descripción del elemento 1"},
        {"id": 2, "nombre": "Elemento 2", "descripcion": "Descripción del elemento 2"}
    ]
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
