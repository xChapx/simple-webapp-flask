import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Bienvenidos!"

@app.route('/como te encuentras')
def hello():
    return 'Muy bien, Como estas tu?'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
