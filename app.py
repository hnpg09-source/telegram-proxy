from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "8393348131:AAED_OTaPlL0rOcm9ffvymcSJwaUP7e8RmY"
CHAT_ID = "6131465835"

@app.route('/send')
def send():
    texto = request.args.get('text', 'sin mensaje')
    texto = texto.replace('+', ' ')
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, json={"chat_id": CHAT_ID, "text": texto})
    return r.text

@app.route('/')
def index():
    return "Proxy activo"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
