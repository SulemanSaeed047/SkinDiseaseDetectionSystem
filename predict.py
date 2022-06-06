from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm, metrics, datasets
from sklearn.utils import Bunch
from sklearn.model_selection import GridSearchCV, train_test_split
import pickle
from skimage.io import imread
from skimage.transform import resize
import skimage
import os
from PIL import Image


def process():
    model=pickle.load(open(os.getcwd()+'\\svm.pkl','rb'))
    labels=['basal cell carcinoma','melanoma','naevus']
    images = []
    flat_data = []
    file=os.listdir(os.getcwd()+'\\static\\img')
    img = skimage.io.imread(os.getcwd()+'\\static\\img\\'+str(file[0]))
    flat_data.append(img.flatten()) 
    images.append(img)
    flat_data = np.array(flat_data)
    images = np.array(images)
    test_data=Bunch(data=flat_data,images=images)
    ans=model.predict(test_data.data) 
    print('Answer-----',ans)  
    print('\n\nOutput : '+labels[ans[0]]+'\n\n')
    
    

    n=labels[ans[0]]
    if n=='melanoma':
        return 'Melanoma/Melanoma is a serious form of skin cancer that begins in cells known as melanocytes. While it is less common than basal cell carcinoma (BCC) and squamous cell carcinoma (SCC), melanoma is far more dangerous because of its ability to spread to other organs more rapidly if it not treated at an early stage.'
    elif n=='naevus':
        return 'Nevus/Nevus (or nevi if multiple) is a nonspecific medical term for a visible, circumscribed, chronic lesion of the skin or mucosa. The term originates from nævus, which is Latin for "birthmark"; however, a nevus can be either congenital (present at birth) or acquired.'
    elif n=='basal cell carcinoma':
        return 'Basal cell carcinoma/Basal cells produce new skin cells as old ones die. Limiting sun exposure can help prevent these cells from becoming cancerous.'
    return 'Error/ Bad input !'