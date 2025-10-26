from flask import Flask
from threading import Thread
import requests
import time

app = Flask('FractalCore AI – KeepAlive')

@app.route('/')
def home():
    return "🟢 FractalCore AI – serveur actif et en veille fractale."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    print("🌀 Serveur Flask lancé pour maintenir FractalCore AI actif.")
    while True:
        try:
            time.sleep(300)
            url = "https://fractalcore-ai-bot.onrender.com"
            requests.get(url)
            print("♻️ Ping envoyé pour garder le bot éveillé.")
        except Exception as e:
            print(f"⚠️ Erreur KeepAlive : {e}")
