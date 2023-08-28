import json
import datetime
import matplotlib.pyplot as plt

with open("cars.json") as obj:
    cars_a = json.load(obj)
cars = cars_a['cars']

with open("customers.json") as obj:
        customer_a = json.load(obj)
customers = customer_a['customers']

with open("sales.json") as obj:
    sales_a = json.load(obj)
sales = sales_a['sales']
car_objs = []
    

class Customer():
    def __init__(self, customer_name="", age=None, email="", rented_car="", rent_days=None, returned=None):
        self.customer_name = customer_name
        self.age = age
        self.email = email
        self.rented_car = rented_car
        self.rent_days = rent_days
        self.returned = returned
        
    def save_info(self, our_index):
        customers[our_index]['Customer Name'] = self.customer_name
        customers[our_index]['Age'] = self.age
        customers[our_index]['Email'] = self.email
        customers[our_index]['Car'] = self.rented_car
        customers[our_index]['Rental Days'] = self.rent_days
        customers[our_index]['Return'] = self.returned
        
        customer_a['customers'][our_index]['Customer Name'] = self.customer_name
        customer_a['customers'][our_index]['Age'] = self.age
        customer_a['customers'][our_index]['Email'] = self.email
        customer_a['customers'][our_index]['Car'] = self.rented_car
        customer_a['customers'][our_index]['Rental Days'] = self.rent_days
        customer_a['customers'][our_index]['Return'] = self.returned
            
        with open("customers.json", 'w') as obj:
            json.dump(customer_a, obj, indent=4)
            
    def delete_info(self, our_index):
        customers[our_index]['Customer Name'] = ""
        customers[our_index]['Age'] = None
        customers[our_index]['Email'] = ""
        customers[our_index]['Car'] = ""
        customers[our_index]['Rental Days'] = None
        customers[our_index]['Return'] = None
        
        customer_a['customers'][our_index]['Customer Name'] = ""
        customer_a['customers'][our_index]['Age'] = None
        customer_a['customers'][our_index]['Email'] = ""
        customer_a['customers'][our_index]['Car'] = ""
        customer_a['customers'][our_index]['Rental Days'] = None
        customer_a['customers'][our_index]['Return'] = None
        
        with open("customers.json", 'w') as obj:
            json.dump(customer_a, obj, indent=4)


with open("sales.json") as obj:
    sales_a = json.load(obj)
sales = sales_a['sales']

def store_sales(price):
    current_month = datetime.datetime.now().strftime("%B")
    if current_month in sales:
        sales[current_month] += price
        sales_a['sales'][current_month] += price
    
    with open('sales.json', 'w') as obj:
        json.dump(sales_a, obj, indent=4)

def display_sales():
    months = [month for month, value in sales.items() if value != 0]
    values = [value for value in sales.values() if value != 0]

    plt.plot(months, values)
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales')
    plt.show()

    exit()
    
store_sales(500)
    
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
            days = int(input("----- DAYS ::: "))
            
            self.customer = Customer(customer_name, age, email, self.car_name, days, self.availability)
            self.customer.save_info(self.car_num)
            cars_a['cars'][carnum]['Availability'] = False
            self.availability = False
            
            store_sales(self.price)
            
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
            self.customer = Customer(rented_car=self.car_name)
            self.customer.save_info(self.car_num)
            self.customer.delete_info(self.car_num)
            
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
    print("6 - Display Sales")
    print("7- Exit")
    print("________________________________________________")

    choice = int(input("----- INPUT ::: "))
    return choice

choice = menu()
while choice != 7:
    if choice == 1:
        
        for i in range(len(car_objs)):
            car_objs[i].display_cars()
            
        carnum = int(input("\n----- CAR NUMBER ::: "))
        search_car(car_objs, carnum)
        input("Press any key to continue...")
        car_objs[carnum].rent_car(carnum)
        
    elif choice == 2:
        
        for i in range(len(car_objs)):
            car_objs[i].unavailable_cars()
            
        carnum = int(input("\n----- CAR NUMBER ::: "))
        car_objs[carnum].return_car(carnum)
        
    elif choice == 3:
        for i in range(len(car_objs)):
            car_objs[i].display_cars()
        
        print("________________________________________________")
        input("Press any key to continue...")
        
    elif choice == 4:
        carnum = int(input("----- CAR NUMBER ::: "))
        search_car(car_objs,carnum)
        input("Press any key to continue...")
        
    elif choice == 5:
        
        for i in range(len(car_objs)):
            car_objs[i].unavailable_cars()
            
        print("________________________________________________")
        input("Press any key to continue...")
        
    elif choice == 6:
        display_sales()
        
    choice = menu()

