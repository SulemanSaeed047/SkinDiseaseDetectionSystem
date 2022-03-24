# SkinDiseaseDetectionSystem
## Contents
*	About Skin Disease Detection System
*	Requirements
    * Hardware Requirements
    * Software Requirements
*	Getting Started
    * Execution Steps
*	Project Process
## About
This system will be able to detect 3 main skin diseases i.e. Melanoma (Skin cancer), Nevus and Basal Cell Carcinoma. We have implemented machine learning techniques for diagnosing Skin Diseases, the input data is an image of the infected skin, and the system will determine the type of the disease.
## Requirements
### Hardware Requirements
1.	Desktop/laptop with internet connection
2.	Minimum 2 GB RAM and 2.5 GB Hard disk while SSD recommended
3.	Camera (can be external or part of device in which will be used for assessing the disease) to get diseased area image. 
### Software Requirements
1.	VS code
2.	Anaconda IDE
3.	Python Interpreter 3.9.7
## Getting Started
Firstly, Install anaconda3 IDE \
Create separate Anaconda Environment in anaconda 3 \
Install Visual Studio Code \
Install important extensions in VS code i.e. Python, Pylance, Jupyter, Open in Browser \
Use python interpreter 3.9.7 with project environment  \
Install Django and easygui from your VS code’s own terminal \
Pull the project from this Github repository in your VS code environment. \
Install the dataset from https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000 \
Place the dataset and change the path of your dataset in your code according to its location \
Install updated versions of necessary Libraries in specified Anaconda Environment which are needed to run the project i.e. TensorFlow, Keras, Numpy, Pandas, OpenCV, Matplotlib, Scikit-learn, Seaborn and all other needed in your environment. We can install libraries from Anaconda IDE directly by selecting specific library needed in the specific environment. \
[Note: Anaconda environment have latest versions of libraries to install]

## Project Process
A Web Application \
Image Input which will show 3 skin diseases results.\
System will Load data, balance it and Augment it.\
Model created to classify the disease.\
Then predicted disease of input image will be shown.

