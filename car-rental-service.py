class Vehicle:
    brand = ""
    model = ""
    year = 0
    __rental_price_per_day = 0

    def __init__(self, brand, model, year, rental_price_per_day) :
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

    def display_info(self) :
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.rental_price_per_day}/day")

    def calculate_rental_cost(self, days) :
        print(f"Rental cost for {self.brand} {self.model} for {days} days: ${days * self.rental_price_per_day}")

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
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.rental_price_per_day}/day")


class Bike (Vehicle):
    engine_capacity = 0

    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}, Rental Price: ${self.rental_price_per_day}/day")


def show_vehicle_info (Vehicle):
    Vehicle.display_info()


myCar = Car ("Honda", "CRV", "2003", 20, 5)

show_vehicle_info(myCar)

# myCar.display_info()
# myCar.calculate_rental_cost(10)

# myCar.set_rental_price_per_day(int(input("Price per day")))
# print(myCar.get_rental_price_per_day())
