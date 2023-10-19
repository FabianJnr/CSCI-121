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