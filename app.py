from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():
    return f"Version 6 - Heure: {datetime.now()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)







