# Làm 1 BE-server nhân chia cộng trừ
from flask import Flask, request
from flask_cors import CORS, cross_origin

#Khởi tạo Flask server BE
app = Flask(__name__)

#Apply flask CORS
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/add", methods = ["POST", "GET"])
@cross_origin(origin="*")
def add_process():
    a = int(request.args.get("sothunhat"))
    b = int(request.args.get("sothuhai"))
    kq = a + b
    return "Result is: " + str(kq)

@app.route("/minus", methods = ["POST", "GET"])
@cross_origin(origin="*")
def minus_process():
    return "Hàm trừ"

@app.route("/viethoa", methods = ["POST"])
@cross_origin(origin="*")
def viethoa():
    #text = request.args.get("chuoiviethoa")
    text = str(request.form.get("chuoiviethoa"))
    return text.upper()  #--> http://127.0.0.1:1909/viethoa?chuoiviethoa=viethoachuoinaydi

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 1909)
