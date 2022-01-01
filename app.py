# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:03:08 2021

@author: arnav
"""
from flask import Flask,render_template,request
import pickle
# import numpy as np
app= Flask(__name__)
model=pickle.load(open('musicrecommendormodel.pkl','rb'))
@app.route('/',methods='GET')
def webpage():
    return render_template('mlmodel.html')
@app.route("/predict",methods=['POST'])
def predictions():
    age=request.form['age']
    gender=request.form['gender']
    prediction=model.predict([[age,gender]])
    output=prediction[0]
    return render_template('mlmodel.html',pred=output)
if __name__=='__main__':
    app.run(debug=True)
