from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():
        return f"Othman EL ALLAOUI Ahlam ELFADLi 2026"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)







   # return f"Version 6 - Heure: {datetime.now()}"
#return f"Version ahlam elfadli and Othman EL ALLAOUI test Heure: {datetime.now()}"