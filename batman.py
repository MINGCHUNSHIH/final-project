from person_c import Person

class Batman(Person):
    def __init__(self, deposit, *args, **kwargs):
        super() .__init__(*args,**kwargs)
        self.deposit = deposit
    
if __name__ == '__main__':
    a = Batman(deposit=1000000,name="Bat",weight=50)
    a.speak()