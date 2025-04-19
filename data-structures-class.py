class Personalinfo():
    def __init__(self, n, t, a, g, j):
        self.name = n
        self.town = t
        self.age = a
        self.gender = g
        self.job = j
    def printinfo(self):
        print(self.name)
        print(self.town)
        print(self.age)
        print(self.gender)
        print(self.job)

object = Personalinfo('Shobhit', 'Online', 24, 'Male', 'Programmer')
print(object.age)
object.printinfo()

class Car(Personalinfo):
    def __init__(self, c, y, cy, h, t):
        self.colour = c
        self.year = y
        self.cylinders = cy
        self.horsepower - h
        self.torque = t
