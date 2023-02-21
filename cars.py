class Car:
    def __init__(self, maxMove=500, maxMovePerTurn=10):
        self.maxMove = maxMove
        self.maxMovePerTurn = maxMovePerTurn
        self.distanceFromShed = 0
        self.distanceTravelled = 0

    def move(self, howFar):
        if howFar > self.maxMovePerTurn:
            howFar = self.maxMovePerTurn
        elif -1*howFar < -1*self.maxMovePerTurn:
             howFar = -1*self.maxMovePerTurn
        self.distanceFromShed += howFar
        self.distanceTravelled += abs(howFar)
        if self.distanceFromShed > self.maxMove:
            overshoot = self.distanceFromShed - self.maxMove
            self.distanceFromShed = self.maxMove
            self.distanceTravelled -= overshoot
        elif self.distanceFromShed < 0:
            overshoot = abs(self.distanceFromShed)
            self.distanceTravelled -= overshoot

    def getDistanceFromShed(self):
        return self.distanceFromShed

    def setDistanceFromShed(self, dist):
        if dist > self.maxMove:
            dist = self.maxMove
        elif dist < 0:
            dist = 0
        self.distanceFromShed = dist

class BondCar(Car):
    def __init__(self, maxMove=500, maxMovePerTurn=20, howManyMissiles=4):
        super().__init__(maxMove, maxMovePerTurn)
        self.howManyMissiles = howManyMissiles

    def launchMissile(self):
        if self.howManyMissiles > 0:
            print("Missiles launched! Kerboom!")
            self.howManyMissiles -= 1
        else:
            print("You are out of missiles, 007.")

    def getHowManyMissilesLeft(self):
        return self.howManyMissiles


James1 = BondCar()
James1.move(20)
James1.move(20)
James1.move(20)

James1.launchMissile()
James1.launchMissile()
James1.launchMissile()
James1.launchMissile()
James1.launchMissile()

print(James1.getDistanceFromShed())


"""
myCar1 = Car(600, 12)
myCar2 = Car(460, 8)
myCar3 = Car()
myCar4 = Car(490)
myCar5 = Car(maxMovePerTurn=12)

myCar1.setDistanceFromShed(590)
myCar1.move(112)
print(myCar1.distanceFromShed)
print(myCar1.distanceTravelled)
myCar1.move(9)
print(myCar1.distanceFromShed)
print(myCar1.distanceTravelled)
myCar1.move(11)
print(myCar1.distanceFromShed)
print(myCar1.distanceTravelled)
myCar1.move(-12)
print(myCar1.distanceFromShed)
print(myCar1.distanceTravelled)
"""

"""
print(myCar1.maxMovePerTurn)
print(myCar2.maxMovePerTurn)
print(myCar3.maxMovePerTurn)
print(myCar4.maxMovePerTurn)
print(myCar1)
"""
