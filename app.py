import flask
from flask import request
from glob import glob
import os


#from predictor import make_prediction

# Initialize the app
app = flask.Flask(__name__, template_folder='templates')


@app.route("/")
def hello():
    """
        Function for rendering the first page
    """
    form_inputs = {'Campaign Name': '',
                   'Campaign Duration': '',
                   'Campaign Goal Amount': '',
                   'Main Category': '',
                   'Backers': ''}


    return flask.render_template('index.html',
                                 form_inputs=form_inputs,
                                 probability='',
                                 prediction='',
                                 SHAP_force_plot='')


@app.route("/about",methods=["POST", "GET"])
def about():
    return flask.render_template('about.html')


@app.route("/contact",methods=["POST", "GET"])
def contact():
    return flask.render_template('contact.html')


#@app.route("/predict", methods=["POST", "GET"])
#def predict():


if __name__=="__main__":
    app.run()