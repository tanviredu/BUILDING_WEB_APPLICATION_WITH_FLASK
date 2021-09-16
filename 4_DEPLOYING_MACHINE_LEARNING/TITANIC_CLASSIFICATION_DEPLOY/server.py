import numpy as np
from flask import Flask,request,jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model1.pkl','rb'))
@app.route("/api",methods=['GET','POST'])
def predict():
    ## get the json response
    data = request.get_json(force=True)
    prediction = model.predict(data['feture'])
    output = "Class "+str(prediction)
    return jsonify(output)


if __name__=="__main__":
    app.run(debug=True)

