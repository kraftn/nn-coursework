# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\крафт\Repositories_And_Code\Python\AI_Methods\Course_Work\gui_application\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.label_directory = QtWidgets.QLabel(self.frame_4)
        self.label_directory.setText("")
        self.label_directory.setObjectName("label_directory")
        self.horizontalLayout.addWidget(self.label_directory)
        self.pushButton_directory = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_directory.sizePolicy().hasHeightForWidth())
        self.pushButton_directory.setSizePolicy(sizePolicy)
        self.pushButton_directory.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_directory.setObjectName("pushButton_directory")
        self.horizontalLayout.addWidget(self.pushButton_directory)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_make = QtWidgets.QComboBox(self.frame)
        self.comboBox_make.setObjectName("comboBox_make")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_make)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_model = QtWidgets.QComboBox(self.frame)
        self.comboBox_model.setObjectName("comboBox_model")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_model)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_segment = QtWidgets.QComboBox(self.frame)
        self.comboBox_segment.setObjectName("comboBox_segment")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_segment)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_transmission = QtWidgets.QComboBox(self.frame)
        self.comboBox_transmission.setObjectName("comboBox_transmission")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_transmission)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_drive_unit = QtWidgets.QComboBox(self.frame)
        self.comboBox_drive_unit.setObjectName("comboBox_drive_unit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_drive_unit)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBox_color = QtWidgets.QComboBox(self.frame)
        self.comboBox_color.setObjectName("comboBox_color")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_color)
        self.label_12 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_12)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 2)
        self.lineEdit_volume = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.gridLayout_3.addWidget(self.lineEdit_volume, 2, 1, 1, 1)
        self.comboBox_fuel_type = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_fuel_type.setObjectName("comboBox_fuel_type")
        self.gridLayout_3.addWidget(self.comboBox_fuel_type, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.frame_3, 3, 1, 1, 1)
        self.pushButton_calc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.gridLayout.addWidget(self.pushButton_calc, 4, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.comboBox_condition = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_condition.setObjectName("comboBox_condition")
        self.gridLayout_2.addWidget(self.comboBox_condition, 1, 1, 1, 1)
        self.lineEdit_mileage = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_mileage.setObjectName("lineEdit_mileage")
        self.gridLayout_2.addWidget(self.lineEdit_mileage, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.dateEdit_year = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_year.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit_year.setCalendarPopup(True)
        self.dateEdit_year.setObjectName("dateEdit_year")
        self.gridLayout_2.addWidget(self.dateEdit_year, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.lineEdit_dollar_to_ruble = QtWidgets.QLineEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_dollar_to_ruble.sizePolicy().hasHeightForWidth())
        self.lineEdit_dollar_to_ruble.setSizePolicy(sizePolicy)
        self.lineEdit_dollar_to_ruble.setObjectName("lineEdit_dollar_to_ruble")
        self.horizontalLayout_2.addWidget(self.lineEdit_dollar_to_ruble)
        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Прогнозирование стоимости автомобиля"))
        self.label_15.setText(_translate("MainWindow", "Служебная директория:"))
        self.pushButton_directory.setText(_translate("MainWindow", "Выбрать"))
        self.label.setText(_translate("MainWindow", "Концерн"))
        self.label_2.setText(_translate("MainWindow", "Модель"))
        self.label_3.setText(_translate("MainWindow", "Сегмент"))
        self.label_4.setText(_translate("MainWindow", "Трасмиссия"))
        self.label_5.setText(_translate("MainWindow", "Привод"))
        self.label_6.setText(_translate("MainWindow", "Цвет"))
        self.label_12.setText(_translate("MainWindow", "Информация о модели"))
        self.label_14.setText(_translate("MainWindow", "Информация о двигателе"))
        self.lineEdit_volume.setText(_translate("MainWindow", "2000"))
        self.label_10.setText(_translate("MainWindow", "Объём (куб. см)"))
        self.label_11.setText(_translate("MainWindow", "Вид"))
        self.pushButton_calc.setText(_translate("MainWindow", "Найти стоимость"))
        self.label_9.setText(_translate("MainWindow", "Дата выпуска"))
        self.label_7.setText(_translate("MainWindow", "Состояние"))
        self.lineEdit_mileage.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "Состояние автомобиля"))
        self.label_8.setText(_translate("MainWindow", "Пробег (км)"))
        self.label_16.setText(_translate("MainWindow", "Курс доллара к рублю"))
        self.lineEdit_dollar_to_ruble.setText(_translate("MainWindow", "73,38"))