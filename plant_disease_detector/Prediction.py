# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\plant disease detector\upload_file v3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from image import image
import pickle
import os
import sys
import numpy as np
import operator
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image
from keras.preprocessing import image as image_utils
from DBconn import DBConnection
import tensorflow as tf


class upload_(object):
    def clear(self):
        self.disease.clear()
        self.remedies_result.clear()
        self.lineEdit.clear()


    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()

    def select_file(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "*.jpg", "*.png")
            # print(fileName)
            self.lineEdit.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[1]
            print(tb.tb_lineno)

    def detection_img(self):
        try:
            test_img=[]
            testimage = self.lineEdit.text()
            if testimage == "null" or testimage == "":
                self.alertmsg("failed", "Please Select the Image")
            else:
                img3 = image.load_img(testimage,target_size=(128, 128))
                img3 = image.img_to_array(img3)
                img3 = img3 / 255
                test_img.append(img3)
                Xtest = np.array(test_img)
                Xtest = Xtest.reshape(len(Xtest), -1)

                model = open('cnn_model.model', 'rb')
                clf_cnn = pickle.load(model)
                predicted = clf_cnn.predict(Xtest)
                result = predicted[0]


                self.disease.setText(result)




        except Exception as e:
            print("Error=" + e.args[1])
            tb = sys.exc_info()[1]
            print("LINE NO: ", tb.tb_lineno)
    def result_rmd(self):
        try:
            val = self.disease.text()
            if val=="" or val=="null":
                self.alertmsg("error", "Please detect the disease first")
            else:
                mydb = DBConnection.getConnection()
                cursor = mydb.cursor()
                query="SELECT Remedies FROM diseases WHERE Dis_Name = '"+val+"' "
                print(query)
                # val = str(dis)
                cursor.execute(query)
                print(cursor)
                result_ = cursor.fetchone()[0]
                print(result_)
                mydb.commit()
                cursor.close()

                # print(result_)
                self.remedies_result.setText(result_)
        except Exception as e:
            print("Error=" + e.args[1])
            tb = sys.exc_info()[2]
            print("LINE NO: ", tb.tb_lineno)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 865)
        Dialog.setStyleSheet("QDialog{background-image: url(:/QDIALOG/backfroun.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 0, 711, 221))
        self.label.setStyleSheet("font: 27pt \"Stencil\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 711, 71))
        self.label_2.setStyleSheet("font: 75 15pt \"Arial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 260, 521, 461))
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(78, 194, 75, 56));")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 400, 158, 43))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(122, 14, 16, 194));")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 401, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 310, 391, 81))
        self.label_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 530, 174, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/detect-removebg-preview.png);\n"
"font: 18pt \"Poor Richard\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(630, 260, 741, 461))
        self.label_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(213, 213, 213, 75));")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(630, 260, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 75 20pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(222, 222, 222, 255));")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.disease = QtWidgets.QLabel(Dialog)
        self.disease.setGeometry(QtCore.QRect(630, 320, 731, 151))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.disease.setFont(font)
        self.disease.setStyleSheet("\n"
"font: 27pt \"Stencil\";\n"
"color: rgb(170, 0, 0);")
        self.disease.setText("")
        self.disease.setAlignment(QtCore.Qt.AlignCenter)
        self.disease.setObjectName("disease")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(630, 490, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 20pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(222, 222, 222, 255));")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.remedies_result = QtWidgets.QLabel(Dialog)
        self.remedies_result.setGeometry(QtCore.QRect(630, 585, 731, 134))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.remedies_result.setFont(font)
        self.remedies_result.setStyleSheet("\n"
"font: 27pt \"Stencil\";\n"
"color: rgb(170, 0, 0);")
        self.remedies_result.setText("")
        self.remedies_result.setAlignment(QtCore.Qt.AlignCenter)
        self.remedies_result.setObjectName("remedies_result")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 610, 174, 61))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/detect-removebg-preview.png);\n"
"font: 18pt \"Poor Richard\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 530, 174, 61))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/detect-removebg-preview.png);\n"
"font: 18pt \"Poor Richard\";")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.select_file)
        self.pushButton_2.clicked.connect(self.detection_img)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.result_rmd)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Plant Disease Detector"))
        self.label_2.setText(_translate("Dialog", "share a picture of Plant Leaf..."))
        self.pushButton.setText(_translate("Dialog", "Select Image"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "No File Chosen"))
        self.label_4.setText(_translate("Dialog", "*Select the Picture"))
        self.pushButton_2.setText(_translate("Dialog", "DETECT"))
        self.label_7.setText(_translate("Dialog", "DISEASE DETECTED>>"))
        self.label_9.setText(_translate("Dialog", "REMEDIES>>"))
        self.pushButton_3.setText(_translate("Dialog", "CLEAR"))
        self.pushButton_4.setText(_translate("Dialog", "REMEDIES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = upload_()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

