from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Kubernetes Jenkins Rollback Project - Version 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)