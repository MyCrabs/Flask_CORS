from flask import Flask, request
from flask_cors import CORS
import tensorflow as tf

###########LOAD KERAS MODEL#############
sess = tf.Session()
graph = tf.get_default_graph()

with sess.as_default():
    with graph.as_default():
        model = load_model("model.h5")

app = Flask(__name__)

CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/classify", methods = ["POST"])
@cross_origin(origin="*")

def process():
    img = request.form.get("img")
    with sess.as_default():
        with graph.as_default():
            name = model.predict()
    return name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = "1909")