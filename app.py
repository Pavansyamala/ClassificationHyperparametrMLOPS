from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np 

from src.pipeline.predictions_pipeline import PredictionPipeline 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-property', methods=['POST'])
def submit_property():

    if request.method == 'POST':

        square_footage = int(request.form['Square_Footage'])
        num_bedrooms = int(request.form['Num_Bedrooms'])
        num_bathrooms = int(request.form['Num_Bathrooms'])
        year_built = int(request.form['Year_Built'])
        lot_size = float(request.form['Lot_Size'])
        garage_size = int(request.form['Garage_Size'])
        neighborhood_quality = int(request.form['Neighborhood_Quality']) 

        values = [square_footage, num_bedrooms, num_bathrooms, year_built, lot_size, garage_size, neighborhood_quality]

        features = ['Square_Footage','Num_Bedrooms','Num_Bathrooms','Year_Built','Lot_Size','Garage_Size','Neighborhood_Quality']

        data_dict = {}
        for i , j in zip(features,values):
            data_dict[i] = j 

        data = pd.DataFrame(data_dict , index=[0])

        print(data)

        predi_pip = PredictionPipeline(data.iloc[:,:])
        prediction = predi_pip.initiate_prediction_pipeline()


        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

