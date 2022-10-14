# this will take the image and predict the results
from keras.models import load_model
from keras.utils.layer_utils import print_summary
import numpy as np
from keras_preprocessing.image import load_img, img_to_array
from keras.applications.vgg19 import preprocess_input
import json
import os
import pandas as pd
baseDir = os.path.join(os.getcwd(), 'trained_model')

print("loading modle here")
model = load_model(os.path.join(baseDir, 'best_model.h5'))

# model shape
print("Model Shape is =>", model.layers[0].input_shape)

data = json.load(open(os.path.join(baseDir, 'datafile.json')))
databaseDir = os.path.join(os.getcwd(), 'data_files')
df = pd.read_csv(open(os.path.join(databaseDir, "supplement_info.csv")))


def prediction(path):
    img = load_img(path, target_size=(256, 256))
    i = img_to_array(img)
    im = preprocess_input(i)
    img = np.expand_dims(im, axis=0)
    pred = np.argmax(model.predict(img))
    value = data[str(pred)]
    print(f" the image belongs to { value } ")
    # return value
    return df.loc[df['disease_name'] == value].values[0][0]


def getDataFromCSV(index):
    if df.shape[0] > index:
        return df.loc[df['index'] == index].values[0]
    else :
        return []



if __name__ == "__main__":
    # just for the testing
    path = os.path.join(baseDir, "baseimg.png")
    print(prediction(path))
