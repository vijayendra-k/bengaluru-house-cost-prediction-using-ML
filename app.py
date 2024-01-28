import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

#procfile.txt 
#web: gunicorn app:app
#first file that we have to run first : flask server name
app = Flask(__name__,static_url_path='/static')
pkl_file = open('finalized_model.pkl','rb')
model = pickle.load(open('finalized_model.pkl', 'rb'))
index_dict = pickle.load(pkl_file)

imagefolder=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=imagefolder
@app.route('/')
def homepage():
    Homepage=os.path.join(app.config['UPLOAD_FOLDER'],'house.jpg')
    return render_template("Homepage.html" , home_image=Homepage)

@app.route('/home',methods=['GET'])
def home():
    #Registration=os.path.join(app.config['UPLOAD_FOLDER'],'Registration.jpg')
    return render_template("Registration.html")

@app.route('/next',methods=['GET'])
def next():
    return render_template("success.html")

@app.route('/back')
def back():
    return render_template("Registration.html")

@app.route('/continue')
def continued():
    return render_template("index.html")
#@app.route('/enterinput')
#def detail():
 #   return render_template('index.html')

    


@app.route('/predict',methods=['POST'])
def predict():

    if request.method=='POST':
        result = request.form

        index_dict = pickle.load(open('cat','rb'))
        location_cat = pickle.load(open('location_cat','rb'))

        new_vector = np.zeros(151)
        #returns a new array with given shape and type with zeros

        result_location = result['location']

        if result_location not in location_cat:
            new_vector[146] = 1
        else:
            new_vector[index_dict[str(result['location'])]] = 1


        new_vector[index_dict[str(result['area'])]] = 1

        new_vector[0] = result['sqft']
        new_vector[1] = result['bath']
        new_vector[2] = result['balcony']
        new_vector[3] = result['size']

    new = [new_vector]

    prediction = model.predict(new)
    #print(prediction)

    return render_template('output.html', Predict_score ='Your house estimate price is  ₹ {} lakhs'.format(prediction))



if __name__ == "__main__":
    app.run(debug=True)
