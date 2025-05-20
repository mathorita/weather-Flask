from flask import Flask,jsonify
from city import get_weather


app = Flask(__name__)

@app.route("/weather/<city>")
def weather(city):
    resultado = get_weather(city)
    if 'erro' in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado)
if __name__ == '__main__':
    app.run(debug=True)