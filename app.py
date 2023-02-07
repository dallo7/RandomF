from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import joblib

#load our model
model = joblib.load("rm")

#make our Flask api...
app = Flask(__name__, template_folder = "template" )

# server = app.server

#form urls/...
@app.route("/")
def home():
    return render_template("rm.html")
    
#Accepting form data
@app.route("/prediction", methods = ["POST"])
def prediction():
    q = request.form["day"] 
    w = request.form["price_of_water"]
    e = request.form["weather"]

# Creating Out of sample instance

    damp = {"day":q, "Price_of_water":w, "weather":e}

    test = pd.DataFrame(damp, index = [289]) # converting the dictonary into Pandas dataframe

    result = model.predict(test) #parsing it to our model for predicting

    result = result[0]

    value = result[0]
    value1 = result[1]
    
#     print(f"Hello, My name is {value } and I'm {value1} years old.")
    
#return prediction, which is the result result.
    return render_template("rm.html", pred = "The Area and Time of day to Distribute water is: {} in the {} ".format(value, value1)) 
    
# Run this file as the main file...
if __name__ == "__main__": 
    app.run(debug = True)
   

            
