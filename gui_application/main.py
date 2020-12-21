import sys
import os
import PyQt5
from PyQt5 import QtWidgets
from main_window import MainWindow


def main():
    pyqt = os.path.dirname(PyQt5.__file__)
    os.environ['QT_PLUGIN_PATH'] = os.path.join(pyqt, "Qt/plugins")

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
