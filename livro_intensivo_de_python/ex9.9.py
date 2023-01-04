class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odomoter(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    @staticmethod
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} -kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range_car = 240
        elif self.battery_size == 85:
            range_car = 270

        message = f"This car can go approximately {range_car} "
        message += "miles on a full charge."

        print(message)

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85


my_tesla = ElectricCar("Tesla", "Model S", 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
