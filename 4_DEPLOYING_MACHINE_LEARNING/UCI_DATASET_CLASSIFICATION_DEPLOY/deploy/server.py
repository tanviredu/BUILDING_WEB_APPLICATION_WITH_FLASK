import numpy as np
from flask import Flask,request,jsonify
import pickle
app = Flask(__name__)
model = pickle.load(open('../model/model.pkl','rb'))
LOOKUP = {0:"NO DIABETIS",1:'DIABETIS'}
@app.route("/api",methods=["GET","POST"])
def predict():
    ## take the json value
    data    = request.get_json(force=True)
    predict = model.predict(data['feature'])
    print(predict)
    output = "Class "+str(predict)
    return jsonify(output) 






if __name__=="__main__":
    app.run(debug=True)