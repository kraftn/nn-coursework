import datetime
import pandas as pd


class Car:
    translation = {'condition': {'С пробегом': 'with mileage', 'Битый': 'with damage',
                                 'На детали': 'for parts'},
                   'fuel_type': {'Бензиновый': 'petrol', 'Дизельный': 'diesel', 'Электрический': 'electrocar'},
                   'color': {'Бордо': 'burgundy', 'Чёрный': 'black', 'Серебристый': 'silver', 'Белый': 'white',
                             'Серый': 'gray', 'Синий': 'blue', 'Фиолетовый': 'purple', 'Красный': 'red',
                             'Зелёный': 'green', 'Коричневый': 'brown', 'Жёлтый': 'yellow', 'Оранжевый': 'orange',
                             'Другой': 'other'},
                   'transmission': {'Механика': 'mechanics', 'Автомат': 'auto'},
                   'drive_unit': {'Передний': 'front-wheel drive', 'Задний': 'rear drive',
                                  'Полный': 'all-wheel drive',
                                  'Подключаемый полный': 'part-time four-wheel drive'}}

    def __init__(self, **kwargs):
        super().__init__()
        self.make = kwargs['make']
        self.model = kwargs['model']
        self.year = kwargs['year']
        self.mileage = kwargs['mileage']
        self.volume = kwargs['volume']
        self.segment = kwargs['segment']

        self.condition = Car.translation['condition'][kwargs['condition']]
        self.fuel_type = Car.translation['fuel_type'][kwargs['fuel_type']]
        self.color = Car.translation['color'][kwargs['color']]
        self.transmission = Car.translation['transmission'][kwargs['transmission']]
        self.drive_unit = Car.translation['drive_unit'][kwargs['drive_unit']]

        now = datetime.datetime.now()
        self.year = now.year - self.year

    def to_dataframe(self):
        data = pd.DataFrame([{'make': self.make, 'model': self.model, 'year': self.year, 'condition': self.condition,
                              'mileage(kilometers)': self.mileage, 'fuel_type': self.fuel_type,
                              'volume(cm3)': self.volume, 'color': self.color, 'transmission': self.transmission,
                              'drive_unit': self.drive_unit, 'segment': self.segment}])
        return data
