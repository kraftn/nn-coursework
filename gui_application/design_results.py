# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\крафт\Repositories_And_Code\Python\AI_Methods\Course_Work\gui_application\results.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_gradient_boosting = QtWidgets.QLabel(Dialog)
        self.label_gradient_boosting.setObjectName("label_gradient_boosting")
        self.verticalLayout.addWidget(self.label_gradient_boosting)
        self.label_random_forest = QtWidgets.QLabel(Dialog)
        self.label_random_forest.setObjectName("label_random_forest")
        self.verticalLayout.addWidget(self.label_random_forest)
        self.label_neural_network = QtWidgets.QLabel(Dialog)
        self.label_neural_network.setObjectName("label_neural_network")
        self.verticalLayout.addWidget(self.label_neural_network)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Результаты"))
        self.label.setText(_translate("Dialog", "Стоимость автомобиля (рубли)"))
        self.label_gradient_boosting.setText(_translate("Dialog", "TextLabel"))
        self.label_random_forest.setText(_translate("Dialog", "TextLabel"))
        self.label_neural_network.setText(_translate("Dialog", "TextLabel"))
