from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QLocale
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import QIntValidator, QDoubleValidator

import design_main_window
from car import Car
from analyzer import Analyzer
from results import ResultsWindow


class MainWindow(QtWidgets.QMainWindow, design_main_window.Ui_MainWindow):
    analyze = pyqtSignal(Car)
    load = pyqtSignal(str, int)
    NUM_FEATURES = 1167

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox_condition.addItems([condition for condition in Car.translation['condition'].keys()])
        self.comboBox_fuel_type.addItems([fuel_type for fuel_type in Car.translation['fuel_type'].keys()])
        self.comboBox_color.addItems([color for color in Car.translation['color'].keys()])
        self.comboBox_transmission.addItems([transmission for transmission in Car.translation['transmission'].keys()])
        self.comboBox_drive_unit.addItems([drive_unit for drive_unit in Car.translation['drive_unit'].keys()])

        self.lineEdit_volume.setValidator(QIntValidator(0, 9999))
        self.lineEdit_mileage.setValidator(QIntValidator(0, 999999))
        validator = QDoubleValidator(0, 999, 2)
        self.lineEdit_dollar_to_ruble.setValidator(validator)

        self.pushButton_calc.clicked.connect(self.calculate)
        self.pushButton_directory.clicked.connect(self.search_directory)

        self.thread = QThread()
        self.analyzer = Analyzer()
        self.analyzer.moveToThread(self.thread)

        self.analyze.connect(self.analyzer.analyze)
        self.load.connect(self.analyzer.load)
        self.analyzer.send_price.connect(self.show_result)
        self.analyzer.send_features.connect(self.set_info)
        self.analyzer.send_file_not_found.connect(self.show_file_not_found)
        self.analyzer.send_not_ready.connect(self.show_not_ready)
        self.analyzer.finished.connect(self.thread.quit)

    def calculate(self):
        if not self.thread.isRunning():
            mileage = self.lineEdit_mileage.text()
            if mileage == '':
                mileage = 0
            volume = self.lineEdit_volume.text()
            if volume == '':
                volume = 2000

            car = Car(make=self.comboBox_make.currentText(), model=self.comboBox_model.currentText(),
                      year=self.dateEdit_year.date().year(), condition=self.comboBox_condition.currentText(),
                      mileage=float(mileage), fuel_type=self.comboBox_fuel_type.currentText(),
                      volume=float(volume), color=self.comboBox_color.currentText(),
                      transmission=self.comboBox_transmission.currentText(), drive_unit=self.comboBox_drive_unit.currentText(),
                      segment=self.comboBox_segment.currentText())
            self.thread.start()
            self.analyze.emit(car)
            self.statusbar.showMessage('Выполняется анализ...')

    def search_directory(self):
        if not self.thread.isRunning():
            directory_path = QFileDialog.getExistingDirectory(self, "Directory Dialog")
            if directory_path != '':
                self.label_directory.setText(directory_path)
                self.thread.start()
                self.load.emit(directory_path, MainWindow.NUM_FEATURES)
                self.statusbar.showMessage('Выполняется загрузка...')

    @pyqtSlot(dict)
    def show_result(self, result):
        self.statusbar.clearMessage()
        coef = self.lineEdit_dollar_to_ruble.text()
        if coef == '':
            coef = 70
        ResultsWindow(result, float(coef.replace(',', '.'))).exec()

    @pyqtSlot(dict)
    def set_info(self, info):
        self.statusbar.clearMessage()
        self.comboBox_make.addItems(sorted(info['make']))
        self.comboBox_model.addItems(info['model'])
        self.comboBox_segment.addItems(sorted(info['segment']))

    @pyqtSlot()
    def show_file_not_found(self):
        self.statusbar.clearMessage()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Один из файлов не найден")
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    @pyqtSlot()
    def show_not_ready(self):
        self.statusbar.clearMessage()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Служебные файлы не загружены")
        msg.setWindowTitle("Ошибка")
        msg.exec_()

