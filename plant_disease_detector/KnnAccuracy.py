import os
import numpy as np
from keras.preprocessing import image
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from keras.models import Sequential
from sklearn.svm import SVC
from Graph import view
import pickle

def calculate_Accuracy_knn():
    print("CALCULATING KNN ACCURACY......")
    # print("[INFO] Loading Training dataset images...")
    DIRECTORY = "..\plant_disease_detector\TestingDataset_accuracy"
    CATEGORIES = ["Apple___healthy", "Apple_Black_rot", "Corn_commonrust", "Corn_healthy", "Grape___healthy",
                  "Grape_Leaf_blight"]

    data = []
    clas = []
    # print("[INFO] Preprocessing...")

    for category in CATEGORIES:
        # print(category)
        path = os.path.join(DIRECTORY, category)
        # print(path)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img = image.load_img(img_path, target_size=(128, 128))
            img = image.img_to_array(img)
            img = img / 255
            data.append(img)
            clas.append(category)

    x_test = np.array(data)
    x_test = x_test.reshape(len(x_test), -1)
    y_test = np.array(clas)
    model = open('..\plant_disease_detector\KNN.model', 'rb')
    clf_knn = pickle.load(model)
    predicted = clf_knn.predict(x_test)
    # print("ppredicted:==",predicted)
    correct = 0
    for x in range(len(x_test)):

        if predicted[x] == y_test[x]:
            correct += 1
    # print("ACCURATE PREDICT", correct)
    accuracy_knn = correct / float(len(x_test)) * 100.0
    return accuracy_knn