import random


# Basic Class And Object
class Car:
    total_car = 0
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
        Car.total_car +=1

    def fullname(self):
        return f'Car Name : {self.brand} & color : {self.color} $ price::{self.price}'

    def Car_ChessiNum(self):
        return f' Car-Chessi-Number :: {random.randint(10000,60000)}'



obj = Car('toyota','corola','200000')
print(obj.fullname())


object = Car('ritz','white','200000')
print(object.fullname())


# Inheritance


class Electrical(Car):
    def __init__(self,brand,model,price,pincode,color):
        super().__init__(brand,model,price)
        self.pincode = pincode
        self.color = color

car = Electrical('ritz','new-ev',60000,591306,'cyan')
print(car.brand, car.color,car.price,car.pincode,)


class EV(Car):
    def __init__(self,brand,price,model,color,Engin):
        super().__init__(brand, color, price)
        self.Engin = Engin
        self.model = model



cars = EV('TATA',2500000,'E-V','Cyan-color','10000RPM')
print(cars.model,cars.Engin,cars.fullname(),cars.Car_ChessiNum())


print(Car.total_car)