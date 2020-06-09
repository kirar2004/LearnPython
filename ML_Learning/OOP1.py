class Robot:
    def __init__(self, rName, rWeight, rColor):
        self.name = rName
        self.weight = rWeight
        self.color = rColor

    def intro(self):
        print('My name is', self.name)


class Person:
    def __init__(self, pName, pLname, pPersonality, pPay):
        self.name = pName
        self.lastname = pLname
        self.personality = pPersonality
        self.fullname = pName + ' ' + pLname
        self.pay = pPay

    def Raise_Pay(self):
        self.pay = self.pay * 1.04


r1 = Robot('Tom', 45, 'Red')
r2 = Robot('Jerry', 65, 'Blue')
p1 = Person('Arun', 'Kantheti', 'Extro', 50000)
p2 = Person('Kiran', 'Kanteti', 'Intro', 60000)

p1.robot_owned = r1
p2.robot_owned = r2
print('My name is', p1.name, 'and I own the robot named', p1.robot_owned.name)
print('My name full name is', p1.fullname)
print('The pay of',p1.name, 'is', p1.pay)
p1.Raise_Pay()
print('The pay after hike is',p1.pay)