class MotorBike:
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear, self.speed))


honda = MotorBike(3, 50)
ducati = MotorBike(1, 10)

print(honda)
print(ducati)



import datetime

today = datetime.datetime.today()

# a human readable interpretation
today.__str__()

today.__repr__()