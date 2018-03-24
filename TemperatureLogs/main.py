from flask import Flask, jsonify, render_template
from source import get


app = Flask(__name__)

@app.route("/get", methods=['GET'])
def lab_env_db():
    return jsonify(get())

@app.route("/show", methods=['GET'])
def show():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)