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

    
class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seating_capacity}")


def show_vehicle_info(vehicle):
    vehicle.display_info()


# Creating instances

car = Car("Toyota", "Corolla", 2020, 50, 5)
bike = Bike("Yamaha", "R1", 2019, 30, 998)

# Displayings details
show_vehicle_info(car)
show_vehicle_info(bike)

# Calculate rental cost
print(f"\nRental cost for {car.brand} {car.model} for 3 days: ${car.calculate_rental_cost(3)}")
print(f"Rental cost for {bike.brand} {bike.model} for 5 days: ${bike.calculate_rental_cost(5)}")

# Modify rental price
car.set_rental_price_per_day(55)
print(f"\nUpdated rental price for {car.brand} {car.model}: ${car.get_rental_price_per_day()}/day")
