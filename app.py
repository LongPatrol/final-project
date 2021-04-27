# import necessary libraries
#from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

import app_model

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    beans = "yay"
    return render_template("homeindex.html",rice=beans)
  # return "Welcome to my 'info' page!"

# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

#Making changes here
@app.route("/results", methods=['POST', 'GET'])
def run_model():
    #book_one, book_two, book_three, book_four, book_five, book_six, book_seven, book_eight, book_nine, book_ten
    print("args:", request.args)
    print("form:", request.values)

    book_one = int(request.values.get("paintedhouse"))
    book_two = int(request.values.get("AngelsDemons"))
    book_three = int(request.values.get("TheLovelyBones"))
    book_four = int(request.values.get("LifeofPi"))
    book_five = int(request.values.get("TheDaVinciCode"))
    book_six = int(request.values.get("DivineSecrets"))
    book_seven = int(request.values.get("TheNannyDiaries"))
    book_eight = int(request.values.get("TheRedTent"))
    book_nine = int(request.values.get("TheSecretLifeofBees"))
    book_ten = int(request.values.get("WildAnimus"))
    
    new_book_data = [[book_one, book_two, book_three, book_four, book_five, book_six, book_seven, book_eight, book_nine, book_ten]]
    predicted_class = app_model.Pickled_book_model.predict(new_book_data)
    
    if predicted_class == 0:
        return "Shoot! The user will not buy Bridget Jones's Diary"
    elif predicted_class == 1:
        return "The user will buy Bridget Jones's Diary. Yay!"
    else:
        return "Something went horribly wrong" 
    
    return "Results page placeholder"
        

if __name__ == "__main__":
    app.run(debug=True)
