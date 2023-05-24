#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:51:21 2023

@author: ram
"""
import numpy as np
from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

app = Flask(__name__)
model = pickle.load(open('loan_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('loan_index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    dict_names={'male':1,'female':0,'yes':1,'no':0,'urban':2,'rural':0,'semiurban':1,'not graduate':0,'notgraduate':0,'graduate':1,'3+':3}
    for i in range(len(int_features)):
        if int_features[i].lower() in dict_names.keys():
            int_features[i]=int(dict_names[int_features[i].lower()])
        else:
            int_features[i]=float(int_features[i])
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if int(prediction)==1:
        i="Approved"
    else:
        i="Declined"
    return render_template('loan_index.html', prediction_text="loan is {}".format(i))
        

if __name__ == "__main__":
    app.run(debug=True)

