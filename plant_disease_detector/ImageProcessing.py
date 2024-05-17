import os
import numpy as np
from keras.preprocessing import image
import sys



def features():
    try:

        print("[INFO] Loading Training dataset images...")
        DIRECTORY = "..\plant_disease_detector\dataset"
        CATEGORIES = ["Apple___healthy","Apple_Black_rot","Corn_commonrust","Corn_healthy","Grape___healthy","Grape_Leaf_blight"]




        data = []
        clas = []
        # print("[INFO] Preprocessing...")

        for category in CATEGORIES:
            print(category)
            path = os.path.join(DIRECTORY, category)
            print(path)
            for img in os.listdir(path):
                img_path = os.path.join(path, img)
                img = image.load_img(img_path, target_size=(128,128))
                img = image.img_to_array(img)
                img = img / 255
                data.append(img)
                clas.append(category)

        # print("[INFO] Features Extraction completed")

        x_train = np.array(data)
        x_train = x_train.reshape(len(x_train), -1)
        y_train = np.array(clas)

        return x_train,y_train
    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)


# features()