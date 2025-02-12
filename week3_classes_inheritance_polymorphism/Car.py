# Car Class Example
class Car:
    def __init__(self, make, model, year, mileage, original_price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.original_price = original_price
        
    def current_value(self, current_year):
        return self.original_price * (.90 ** (current_year - self.year))
        
    def __str__(self):
        return str(self.year) + " " + self.make + " " + self.model 
    
class AntiqueCar(Car):
    def current_value(self, current_year):
        return self.original_price * (1.01 ** (current_year - self.year))



def main():
    #instantiate class, and give a short example


main()


andys_car = Car("Toyota", "Sequoia", 2001, 305000, 40000)

chris_car = Car("Honda", "Fit", 2009, 132000, 14000)

alex_car = Car("Nissan", "Altima", 2017, 74000, 25000)

marshall_car = Car("Saturn", "SW2", 1997, 290000, 12000)

print(andys_car)

print(andys_car.current_value(2025))

andys_car_lot = [andys_car, chris_car, alex_car, marshall_car]

# calculate total value of all cars
value = 0.0
for car in andys_car_lot:
    value += car.current_value(2025)

print("lot total value: ", value)

andys_dream_car = AntiqueCar("Cadillac", "DeVille Convertible", 1978, 120000, 10000)

mac_dream_car = AntiqueCar("Suzuki", "Carry", 2002, 100000, 8000)

andys_car_lot.append(andys_dream_car)
andys_car_lot.append(mac_dream_car)

# calculate total value of all cars
total_value = 0.0
for car in andys_car_lot:
    total_value += car.current_value(2025)

print("lot total value: ", total_value)