import numpy as np
from flask import Flask, request, jsonify
import hyper as hp
import flask
import json
import io
import utils
from flaskext.mysql import MySQL
from flask_cors import CORS

# Khởi tạo model.

global DOT
global COSINE
global products
global embeddings

DOT = 'dot'
COSINE = 'cosine'
products = None
embeddings = None

# Khởi tạo flask app
app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hoctap1234'
app.config['MYSQL_DATABASE_DB'] = 'clothai'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)

@app.route("/", methods=["GET"])
def _hello_world():
	return "Hello world"

@app.route("/predict", methods=["POST"])
def _preddict():
    json_data = flask.request.json
    item_name = json_data['item_name']

    conn = mysql.connect()
    cursor = conn.cursor()

    query = "select * from clothai5000.products where name = %s"
    param = (item_name)  
    cursor.execute(query,param)
    item = cursor.fetchone()
    item_id = item[0]

    indices = utils._product_similarity(products, embeddings,product_id=item_id, measure=COSINE, k=20)

    query = "select * from clothai5000.products where product_id = %s"
    names = []
    images = []
    links = []
    ids = []
    pricesold = []
    prices = []
    discounts = []

    for item_id in indices:
      param = (item_id)
      cursor.execute(query,param)
      item = cursor.fetchone()
      ids.append(item[0])
      names.append(item[1])
      links.append(item[2])
      images.append(item[3])
      pricesold.append(item[4])
      prices.append(item[5])
      discounts.append(item[6])
    
    data = {"ids":ids,"names":names,"links":links,"images":images,
    "pricesold":pricesold,"prices":prices,"discounts":discounts}
    return jsonify(data)

if __name__ == "__main__":
	print("App run!")
	# Load model
	products, embeddings = utils._load_model_data()
	app.run(debug=True)