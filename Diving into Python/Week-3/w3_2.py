from pathlib import Path
import os
import csv

def get_car_list(csv_file_name):
    car_list = []
    with open(csv_file_name) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for i in reader:
            if i['car_type'] != '' and i['brand'] != '' and len(Path(i['photo_file_name']).suffixes) == 1 and i['carrying'] != '':
                try:
                    if i['car_type'] == 'car':
                        car_list.append(Car(i['brand'], i['photo_file_name'], i['carrying'], i['passenger_seats_count']))
                    elif i['car_type'] == 'truck':
                        car_list.append(Truck(i['brand'], i['photo_file_name'], i['carrying'], i['body_whl']))
                    elif i['car_type'] == 'spec_machine' and i['extra'] != '':
                         car_list.append(SpecMachine(i['brand'], i['photo_file_name'], i['carrying'], i['extra']))
                except:
                    continue
    return car_list


class CarBase:
    """Базовий клас всіх типів машин"""
    
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        
    def get_photo_file_ext(self):
        root_ext = os.path.splitext(self.photo_file_name)
        return root_ext[1]

    
class Car(CarBase):
    """Легкові автомобілі"""
    
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"

        
class Truck(CarBase):
    """Грузові автомобілі"""
    
    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"        
        self.body_whl = body_whl
        
        try:
            # Відокремлення довжини, широти і висоти
            self._string_text_1 = self.body_whl.partition('x')
            self.body_length = float(self._string_text_1[0])
            self._string_text_2 = self._string_text_1[2].partition('x')
            self.body_width = float(self._string_text_2[0])    
            self.body_height = float(self._string_text_2[2])
        
        except:
            self.body_length = 0.0        
            self.body_width = 0.0        
            self.body_height = 0.0
        
    def get_body_volume(self):
        return (self.body_length * self.body_width * self.body_height)

    
class SpecMachine(CarBase):
    """Спецтехніка"""
    
    def __init__(self, brand, photo_file_name, carrying, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra
        