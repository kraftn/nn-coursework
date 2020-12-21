from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import torch
import joblib
import xgboost
import os
import json

from car import Car
from neural_network import RegressionNet


class Analyzer(QObject):
    finished = pyqtSignal()
    send_price = pyqtSignal(dict)
    send_features = pyqtSignal(dict)
    send_file_not_found = pyqtSignal()
    send_not_ready = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.col_transformer = None
        self.scaler = None
        self.grad_boosting = None
        self.random_forest = None
        self.neural_network = None
        self.is_ready = False

    @pyqtSlot(Car)
    def analyze(self, car):
        if self.is_ready:
            features = self.col_transformer.transform(car.to_dataframe())
            scaled_features = torch.from_numpy(self.scaler.transform(features.toarray())).float()
            result = {'grad_boosting': self.grad_boosting.predict(xgboost.DMatrix(features))[0],
                      'random_forest': self.random_forest.predict(features)[0],
                      'neural_network': self.neural_network.forward(scaled_features).item()}
            self.send_price.emit(result)
        else:
            self.send_not_ready.emit()
        self.finished.emit()

    @pyqtSlot(str, int)
    def load(self, directory_path, num_features):
        try:
            self.col_transformer = joblib.load(os.path.join(directory_path, 'column_transformer.joblib'))
            self.scaler = joblib.load(os.path.join(directory_path, 'min_max_scaler.joblib'))
            self.grad_boosting = xgboost.Booster()
            self.grad_boosting.load_model(os.path.join(directory_path, 'grad_boosting.model'))
            self.random_forest = joblib.load(os.path.join(directory_path, 'random_forest.joblib'))
            self.neural_network = RegressionNet(num_features)
            self.neural_network.load_state_dict(torch.load(os.path.join(directory_path, 'neural_network.pt'),
                                                map_location=torch.device('cpu')))
            self.neural_network.eval()
            with open(os.path.join(directory_path, 'categorial_features.json'), 'r') as f:
                cat_features = json.load(f)
        except FileNotFoundError:
            self.is_ready = False
            self.send_file_not_found.emit()
        else:
            self.is_ready = True
            self.send_features.emit(cat_features)
        finally:
            self.finished.emit()

