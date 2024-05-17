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
from KnnAccuracy import calculate_Accuracy_knn
from Svm_Accuracy import calculate_svm_accuracy
from CnnAccuracy import calculate_cnn_accuracy
def calculate_Accuracy():
    svc_accuracy = calculate_svm_accuracy()
    knn_accuracy = calculate_Accuracy_knn()
    cnn_accuracy = calculate_cnn_accuracy()
    print("SVM ACCURACY",svc_accuracy)
    print("KNN ACCURACY",knn_accuracy)
    print("CNN ACCURACY",cnn_accuracy)

    list = []
    list.clear()
    list.append(svc_accuracy)
    list.append(knn_accuracy)
    list.append(cnn_accuracy)
    view(list)
# calculate_Accuracy()