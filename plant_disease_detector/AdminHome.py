# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\plant disease detector\admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image.image
from ImageProcessing import features
from BuildModel import build_model
from AlgorithmPerformance import calculate_Accuracy


class admin_(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()
    def imgprocessing(self):
        self.x_train,self.y_train=features()
        self.alertmsg("Successfull","Image processing completed successfully")
    def build_models(self):
        print("x_train",self.x_train)
        print("y_train",self.y_train)
        build_model(self.x_train,self.y_train)
        self.alertmsg("Successfull", "Models are Build Successfully")

    def analysis(self):
        calculate_Accuracy()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 863)
        Dialog.setStyleSheet("QDialog{background-image: url(:/QDIALOG/backfroun.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(480, 170, 521, 631))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(26, 138, 13, 94), stop:1 rgba(255, 255, 255, 255));")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 630, 211, 61))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("font: 63 14pt \"Lucida Fax\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 145, 0, 90), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 510, 211, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 63 14pt \"Lucida Fax\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 145, 0, 90), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(640, 390, 211, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 63 14pt \"Lucida Fax\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 145, 0, 90), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(486, 177, 508, 91))
        self.label_2.setStyleSheet("font: 63 22pt \"Lucida Fax\";\n"
"font: 26pt \"Elephant\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 160, 14, 239), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(905, 181, 91, 91))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/admin.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.imgprocessing)
        self.pushButton_2.clicked.connect(self.build_models)
        self.pushButton_4.clicked.connect(self.analysis)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_4.setText(_translate("Dialog", "Analysis"))
        self.pushButton_2.setText(_translate("Dialog", "Build\n""Classifier"))
        self.pushButton.setText(_translate("Dialog", "Image\n""Processing"))
        self.label_2.setText(_translate("Dialog", "ADMIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = admin_()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
