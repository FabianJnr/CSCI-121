import math

class Car():
    def __init__(self, mpg, fuelcap, money):
        self.mpg = mpg
        self.fuelcap = fuelcap
        self.fuel = fuelcap
        self.money = money
        self.x = 0
        self.y = 0
        
    def driveTo(self, x, y):
        distance = math.sqrt((x-self.x)**2 + (y-self.y)**2)
        if (self.mpg * self.fuel) < distance:
            return False
        else:
            self.x = x
            self.y = y
            self.fuel -= distance / self.mpg 
            return True
    def getLocation(self):
        return [self.x, self.y]
    
    def getGas(self):
        return self.fuel
    
    def getToFill(self):
        return self.fuelcap - self.fuel
    
    def getMoney(self):
        return self.money
    
    def pay(self, amount):
        self.money -= amount
        
    def reFill(self):
        self.fuel = self.fuelcap
        
class GasStation():
    def __init__(self, x, y, charges):
        self.x = x
        self.y = y
        self.charges = charges
    
    def refillCar(self, car):
        location = car.getLocation()
        cost_to_refill = car.getToFill() * self.charges
        if cost_to_refill > car.getMoney() or (math.sqrt(self.x**2 + self.y**2) - math.sqrt(location[0]**2 + location[1]**2)) >= 0.001:
            return False
        else:
            car.pay(cost_to_refill) 
            car.reFill()
            return True

class Taxi(Car):
    def __init__(self, mpg, fuelcap, money):
        super().__init__(mpg, fuelcap, money)
        self.passenger = False
        self.passenger_distance = 0
        
    def pickup(self):
        if self.passenger == True:
            return False
        else:
            self.passenger = True
            return True
    
    def driveTo(self, x, y):
        distance = math.sqrt((x-self.x)**2 + (y-self.y)**2)
        if (self.mpg * self.fuel) < distance:
            return False
        else:
            if self.passenger:
                self.passenger_distance += distance
            self.x = x
            self.y = y
            self.fuel -= distance / self.mpg 
            return True
        
    def dropoff(self):
        if self.passenger == True:
            self.passenger = False
            self.money += 3* self.passenger_distance + 2
            self.passenger_distance = 0
            return True
        else:
            return False


class Dispatcher():
    def __init__(self):
        self.fleet = []
        
    def hire(self):
        self.fleet.append(self)
        
    def hail(self, x, y):
        min_distance = float('inf')
        right_taxi = None
        for taxi in self.fleet:
            if taxi.passenger == False:
                distance = math.sqrt((x - taxi.x)**2 + (y-taxi.y)**2)
                if taxi.fuel >= distance:
                    if distance < min_distance:
                        min_distance = distance
                        right_taxi = taxi
        if right_taxi == None:
            return None
        right_taxi.driveTo(x, y)
        right_taxi.pickup()
        return None
