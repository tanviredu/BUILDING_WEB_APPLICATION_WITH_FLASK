import numpy as np
from flask import Flask,request,jsonify
import pickle

app   = Flask(__name__)
model = pickle.load(open('model1.pkl','rb')

@app.route('/api',methods=['POST'])
def predict():
    ## get the json
    data        = request.get_json(force=True)
    prediction  = model.predict(data['feature'])
    output = "Survived: "+str(prediction)

if __name__=='__main__':
    app.run(port=8000,debug=True)
