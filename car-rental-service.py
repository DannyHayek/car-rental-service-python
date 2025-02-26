class Vehicle:
    brand = ""
    model = ""
    year = 0
    rental_price_per_day = 0

    def __init__(self, brand, model, year, rental_price_per_day) :
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

    def display_info(self) :
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.rental_price_per_day}/day")

    def calculate_rental_cost(self, days) :
        
        print(f"Rental cost for {self.brand} {self.model} for {days} days: ${days * self.rental_price_per_day}")

class VehicleExpanded (Vehicle) :
    seating_capacity = 0

    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity


#class Bike (Vehicle):

myCar = VehicleExpanded ("Honda", "CRV", "2003", 20, 5)

myCar.display_info()
myCar.calculate_rental_cost(10)
print(myCar.seating_capacity)
