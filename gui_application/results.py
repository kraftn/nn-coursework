from PyQt5 import QtWidgets
import design_results


class ResultsWindow(QtWidgets.QDialog, design_results.Ui_Dialog):
    def __init__(self, results, coef):
        super().__init__()
        self.setupUi(self)
        self.label_gradient_boosting.setText('Градиентный бустинг: {:.0f}'.format(coef*results['grad_boosting']))
        self.label_random_forest.setText('Случайный лес: {:.0f}'.format(coef*results['random_forest']))
        self.label_neural_network.setText('Нейронная сеть: {:.0f}'.format(coef*results['neural_network']))
