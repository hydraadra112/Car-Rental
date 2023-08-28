import json
import datetime
import matplotlib.pyplot as plt

with open("cars.json") as obj:
    cars_a = json.load(obj)
cars = cars_a['cars']
car_objs = []

with open("sales.json") as obj:
    sales_a = json.load(obj)
sales = sales_a['sales']

class Customer():
    def __init__(self, customer_name, age, email, rented_car, rent_days, returned):
        self.customer_name = customer_name
        self.age = age
        self.email = email
        self.rented_car = rented_car
        self.rent_days = rent_days
        self.returned = returned
        self.save_info()
        
    def save_info(self):
        with open("customers.json", "w") as obj:
            customer_a = json.load(obj)
        customers = customer_a['customers']
        for i in range(len(customers)):
            customers[i]['Customer Name'] = self.customer_name
            customers[i]['Age'] = self.age
            customers[i]['Email'] = self.email
            customers[i]['Car'] = self.rented_car
            customers[i]['Rental Days'] = self.rent_days
            customers[i]['Return'] = self.returned
            

class Car():
    def __init__(self, car_name, srn, pltn, price, availability, car_num):
        self.car_name = car_name
        self.srn = srn
        self.pltn = pltn
        self.price = price
        self.availability = availability
        self.car_num = car_num
        
    def rent_car(self, carnum):
        if self.availability == True:
            print("________________________________________________")
            print("              INFORMATION SHEET")
            customer_name = input("----- NAME ::: ")
            age = int(input("----- AGE ::: "))
            email = input("----- EMAIL ::: ")
            days = input("----- DAYS ::: ")
            self.customer = Customer(customer_name, age, email, self.car_name, days, self.availability)
            cars_a['cars'][carnum]['Availability'] = False
            self.availability = False
            with open("cars.json", "w") as obj:
                json.dump(cars_a, obj, indent=4)
            print(f"\n{self.car_name} rented succesfully")
            input("Press any key to continue...")
        else:
            print(f"\n{self.car_name} is currently unavailable")
            input("Press any key to continue...")
            
    def return_car(self, carnum):
        if self.availability == False:
            cars_a['cars'][carnum]['Availability'] = True
            self.availability = True
            with open("cars.json", "w") as obj:
                json.dump(cars_a, obj, indent=4)
            print(f"\n{self.car_name} returned succesfully")
            input("Press any key to continue...")
        else:
            print(f"\n{self.car_name} is available")
            input("Press any key to continue...")
            
    def display_cars(self):
        if self.availability == True:
            print("________________________________________________")
            print(f"CAR NUMBER           : {self.car_num}")
            print(f"CAR NAME             : {self.car_name}")
            print(f"AVAILABILITY         : {'Available' if self.availability else 'Not Available'}")
            print("------------------------------------------------")
        else:
            return
    def unavailable_cars(self):
        if self.availability == False:
            print("________________________________________________")
            print(f"CAR NUMBER           : {self.car_num}")
            print(f"CAR NAME             : {self.car_name}")
            print(f"AVAILABILITY         : {'Available' if self.availability else 'Not Available'}")
            print("------------------------------------------------")
        else:
            return
        
for car in cars:
    """ Making a list of objects of class Car """
    car_objs.append(Car(car['Car Name'], car['Serial Number'], car['Plate Number'], car['Price'], car['Availability'], car['Car Number']))

def search_car(car_objs, specific_car):
    """ Searching a specific car and its details """
    print("________________________________________________")
    for index, car in enumerate(car_objs):
        if index != specific_car:
            continue
        else:
            print(f"CAR NUMBER           : {car.car_num}")
            print(f"CAR NAME             : {car.car_name}")
            print(f"SERIAL KEY           : {car.srn}")
            print(f"PLATE                : {car.pltn}")
            print(f"PRICE                : {car.price}")
            print(f"AVAILABILITY         : {'Available' if car.availability else 'Not Available'}")
    print("________________________________________________")

def menu():
    print("________________________________________________")
    print("            Welcome to Car Rental")
    print("1 - Rent Car")
    print("2 - Return Car")
    print("3 - Available Cars")
    print("4 - Search Car")
    print("5 - Used Cars")
    print("6 - Exit")
    print("________________________________________________")

    choice = int(input("----- INPUT ::: "))
    return choice

current_month = datetime.datetime.now().strftime("%B")
wah = sales_a['sales'][current_month] + 5500

print(wah)

