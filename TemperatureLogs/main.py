import time
from datetime import datetime

from flask import Flask, jsonify, render_template, request

from database import get

app = Flask(__name__)


@app.route("/get", methods=['GET'])
def get_data():
    date_from = request.args.get('from', time.strftime("%Y-%m-%d 00:00"))
    date_to = request.args.get('to', time.strftime("%Y-%m-%d %H:%M"))
    if date_from == u'null' and  date_to == u'null':
        date_from = datetime.now().strftime('%Y-%m-%d 00:00:00')
    return jsonify(get(date_from, date_to))


@app.route("/show", methods=['GET'])
def show_data():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
