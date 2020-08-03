from person_c import Person

class spiderman(Person):
    def __init__(self, str, *args, **kwargs):
        super() .__init__(*args,**kwargs)
        self.str=str
    def climb(self):
        self.str-=1
        print(self.str)
    
if __name__ == '__main__':
    s = spiderman(str=100,name="sss", weight=50)
    s.climb()