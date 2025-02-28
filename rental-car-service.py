class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model},
            Year: {self.year}, Rental Price: ${self.__rental_price_per_day} / day")

    def calculate_rental_cost(self, days):
        return days * self.__rental_price_per_day

    #getter and seetter for rental price per day due to private declaration
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

    def set_rental_price_per_day(self, new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Invalid price it should be greater than zero")


class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info() 
        print(f"Engine: {self.engine_capacity}cc")

    
