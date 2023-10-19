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