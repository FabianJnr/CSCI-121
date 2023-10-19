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
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            return False
        
    def reFill(self):
        self.fuel = self.fuelcap
        
class GasStation():
    def __init__(self, x, y, charges):
        self.x = x
        self.y = y
        self.charges = charges
    
    def refillCar(self, car):
        distance = ((self.x -car.x)**2 + (self.y - car.y)**2)**0.5
        if distance > 0.001:
            return False
        else:
            cost_to_fill = car.getToFill() * self.charges
            if car.pay(cost_to_fill):
                car.reFill()
                return True
            return False