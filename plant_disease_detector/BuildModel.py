import os
from ImageProcessing import features
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
import pickle
from sklearn.svm import SVC
import sys
from CnnModel_2 import CNN_BULDMODEL

def build_model(x_train,y_train):
    try:
        #KNN
        print("[INFO] Training KNN model...")
        clf_knn = KNeighborsClassifier()
        clf_knn.fit(x_train, y_train)
        with open('KNN.model', 'wb') as f:
            pickle.dump(clf_knn, f)
        print("[INFO] Training KNN model created successfully..!")

        #SVM
        print("[INFO] Training SVM model...")
        clf_svm = LinearSVC(multi_class='crammer_singer')
        print(clf_svm)
        clf_svm.fit(x_train, y_train)
        print(clf_svm)
        with open('SVM.model', 'wb') as f:
            pickle.dump(clf_svm, f)
        print("[INFO]  Training SVM model created successfully..!")

        #CNN
        CNN_BULDMODEL()
        print("CNN Model Build Successfully")



    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)



