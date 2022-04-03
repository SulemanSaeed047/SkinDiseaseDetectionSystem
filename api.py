import os 
import uuid
import flask 
import urllib
from PIL import Image
from tensorflow.keras.models import load_model
from flask import Flask , render_template  , request , send_file
from tensorflow.keras.preprocessing.image import load_img , img_to_array
app = Flask(__name__)

#way to upload image
#way to save the image
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load_model(os.path.join(BASE_DIR , 'model.hdf5'))
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT
    classes = [ 'Basal cell carcinoma',   'melanoma' ,'nevus' ]
def predict(filename , model):
    img = load_img(filename , target_size = (64 , 64))
    img = img_to_array(img)
    img = img.reshape(1 , 64 ,64 ,3)
    img = img.astype('float32')
    img = img/255.0
    result = model.predict(img)
    dict_result = {}
    for i in range(3):
        dict_result[result[0][i]] = classes[i]
    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:3]
    
    prob_result = []
    class_result = []
    for i in range(3):
        prob_result.append((prob[i]*100).round(2))
        class_result.append(dict_result[prob[i]])
    return class_result , prob_result