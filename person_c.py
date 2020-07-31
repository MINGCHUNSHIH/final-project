class Person:

    def __init__(self, name, weight, H=188, fat_rate=1):
        self.name = name
        self.weight = weight
        self.High= H
        self.rate = fat_rate

    def eat(self):
        self.weight += self.rate

    def exercise(self):
        self.weight -= self.rate

    def speak(self):
        print('%s, weight: %d ,%d' % (self.name, self.weight, self.High))
    def health(self):
        return self.weight,self.High
def BMI(h,w):
    print(w/(h/100)**2)

if __name__ == '__main__':
    p1 = Person(name='Kevin', weight=50, fat_rate=3)
    '''p1.eat()
    p1.eat()
    p1.speak()
    p1.exercise()
    p1.speak()'''
    w,h=p1.health()
    BMI(h,w)

    '''p2 = Person('K', 50, fat_rate=2)
    p2.eat()
    p2.eat()
    p2.speak()
    p2.exercise()
    p2.speak()
    
    p3 = Person('Ke', 60)
    p3.eat()
    p3.eat()
    p3.speak()
    p3.exercise()
    p3.speak()'''
    
    