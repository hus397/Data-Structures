class Personalinfo():
    __password = 'abc123'
    def __init__(self, n, t, a, g, j):
        self.name = n
        self.town = t
        self.age = a
        self.gender = g
        self.job = j
    def printinfo1(self):
        print(self.name)
        print(self.town)
        print(self.age)
        print(self.gender)
        print(self.job)
        print(self.__password)   

object = Personalinfo('Shobhit', 'Online', 24, 'Male', 'Programmer')
print(object.age)
object.printinfo1()

class Car(Personalinfo):
    def __init__(self, c, y, cy, h, tq, n, t, a, g, j):
        super().__init__(n, t, a, g, j)
        self.colour = c
        self.year = y
        self.cylinders = cy
        self.horsepower = h
        self.torque = tq
    def printinfo(self):
        print(self.colour)
        print(self.year)
        print(self.cylinders)
        print(self.horsepower)
        print(self.torque)
        #super().printinfo()
        
#voiture = Car('Green', '2008', '3', '216', '400', 'Shobhit', 'Online', '24', 'Male', 'Programmer')
#voiture.printinfo1()

def addnat(n):
    global sum1
    sum1 = 0
    for i in range(1, n+1):
        sum1 = sum1 + i
        
addnat(10)
print(sum1)
