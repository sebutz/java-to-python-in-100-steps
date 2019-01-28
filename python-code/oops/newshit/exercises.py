class MotorBike:

    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear, self.speed))


mb1 = MotorBike("Suzuki", 330.00)
mb2 = MotorBike("Yamaha", 340.00)

print(mb1)
print(mb2)
