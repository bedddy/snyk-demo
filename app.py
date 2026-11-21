from flask import Flask
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")

@app.route("/")
def home():
    return "Bonjour, Caplogy !"

if __name__ == "__main__":
    app.run(debug=True)