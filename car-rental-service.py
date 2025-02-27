class Vehicle:
    brand = ""
    model = ""
    year = 0
    __rental_price_per_day = 0

    def __init__(self, brand, model, year, rental_price_per_day) :
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def display_info(self) :
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.get_rental_price_per_day()}/day")

    def calculate_rental_cost(self, days) :
        print(f"Rental cost for {self.brand} {self.model} for {days} days: ${days * self.get_rental_price_per_day()}")

    def set_rental_price_per_day(self, price) :
        self.__rental_price_per_day = price

    def get_rental_price_per_day(self) :
        return self.__rental_price_per_day

class Car (Vehicle) :
    seating_capacity = 0

    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price_per_day}/day")


class Bike (Vehicle):
    engine_capacity = 0

    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}, Rental Price: ${self.get_rental_price_per_day}/day")


def show_vehicle_info (Vehicle):
    Vehicle.display_info()

def options ():
    print("Welcome to your vehicle rental service manager!")
    print("Enter the number for the action you wish to take.")
    print("1: Show cars")
    print("2: Show bikes")
    print("3: Calculate rental costs for a vehicle")
    print("4: Modify rental costs for a vehicle")
    print("5: Exit the manager")

    return int(input("Which option do you wish to perform: "))


car1 = Car ("Honda", "CRV", "2003", 10, 5)
car2 = Car ("Mitsubishi", "Outlander", "2014", 30, 7)
car3 = Car ("Toyota", "FJ Cruiser", 2020, 50, 4)

bike1 = Bike ("Yamaha", "R1", "2019", 35, 998)
bike2 = Bike ("Harley-Davidson", "Fat Boy", "2012", 60, 1584)
bike3 = Bike ("Kawasaki", "Ninja", "2008", 50, 798)

myCars = [car1, car2, car3]
myBikes = [bike1, bike2, bike3]

print("===========================================\n")

show_vehicle_info(car1)
show_vehicle_info(car2)
show_vehicle_info(car3)

print("\n===========================================\n")

show_vehicle_info(bike1)
show_vehicle_info(bike2)
show_vehicle_info(bike3)

print("\n===========================================")

print(bike1.calculate_rental_cost(10))

# option = 0

# while option != 5 :
#     if option == 0:
#         option = options()

#     if option == 1:
#         for car in myCars :
#             show_vehicle_info(car)

#     option = 0
    
