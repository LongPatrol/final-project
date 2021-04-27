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
    return render_template("homeindex.html")
  # return "Welcome to my 'info' page!"

# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

#Making changes here
@app.route("/results/<book_one>/<book_two>/<book_three>/<book_four>/<book_five>/<book_six>/<book_seven>/<book_eight>/<book_nine>/<book_ten>")
def run_model(book_one, book_two, book_three, book_four, book_five, book_six, book_seven, book_eight, book_nine, book_ten):

#@app.route("/results")
#def about():
    #10 parameters for the 10 books we're using instead of the username and password
    #username = request.args.get('username')
    #password = request.args.get('password')

    #Do prediction here: take values from parameters; 
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
