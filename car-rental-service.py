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


myCar = Vehicle("Honda", "CRV", "2003", 20)

myCar.display_info()
