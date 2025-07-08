class Vehicle:
    total_vehicles = {}

    def __init__(self, make, colour, year, price):
        self.make = make
        self.colour = colour
        self.year = year
        self.price = price
        Vehicle.total_vehicles.setdefault(make, []).append(self)

    def __repr__(self):
        return f"Vehicle({self.make}, {self.colour}, {self.year}, {self.price})"

class Car(Vehicle):
    total_cars = {}

    def __init__(self, make, colour, year, price, size):
        super().__init__(make, colour, year, price)
        self.size = size
        Car.total_cars.setdefault(make, []).append(self)

    def __repr__(self):
        return f"Car({self.make}, {self.colour}, {self.year}, {self.price}, {self.size})"

class Bike(Vehicle):
    total_bikes = {}

    def __init__(self, make, colour, year, price, bike_type):
        super().__init__(make, colour, year, price)
        self.bike_type = bike_type
        Bike.total_bikes.setdefault(make, []).append(self)

    def __repr__(self):
        return f"Bike({self.make}, {self.colour}, {self.year}, {self.price}, {self.bike_type})"

class Truck(Vehicle):
    total_trucks = {}

    def __init__(self, make, colour, year, price, duty):
        super().__init__(make, colour, year, price)
        self.duty = duty
        Truck.total_trucks.setdefault(make, []).append(self)

    def __repr__(self):
        return f"Truck({self.make}, {self.colour}, {self.year}, {self.price}, {self.duty})"

class Customer:
    total_customers = {}

    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        Customer.total_customers[self.customer_id] = self

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.first_name}, {self.last_name})"

class RentalService:
    def __init__(self):
        self.rented_vehicles = []

    def rent_vehicle(self):
        vehicle_type = input("Input the type of vehicle (car, bike, truck): ").strip().lower()

        if vehicle_type not in ["car", "bike", "truck"]:
            print("We do not have that kind of vehicle.")
            return

        make = input(f"Input the make of the {vehicle_type}: ").strip()
        
        vehicle_dict = {
            "car": Car.total_cars,
            "bike": Bike.total_bikes,
            "truck": Truck.total_trucks
        }

        available = vehicle_dict[vehicle_type].get(make)
        
        if not available:
            print(f"No available {vehicle_type}s of make '{make}'.")
            return

        print(f"{vehicle_type.capitalize()} rented successfully: {available[0]}")
        self.rented_vehicles.append(available.pop(0))

# Example:
# Adding vehicles
Car("Toyota", "Red", 2020, 25000, "Compact")
Bike("Yamaha", "Black", 2022, 1500, "Sport")
Truck("Volvo", "Blue", 2019, 45000, "Heavy-duty")

# Using rental service
service = RentalService()
service.rent_vehicle()
