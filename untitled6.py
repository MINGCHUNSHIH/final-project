from spiderman import spiderman
from batman import Batman
class superman(spiderman,Batman):
    def __init__(self, *args, **kwargs):
        super() .__init__(*args,**kwargs)
if __name__ == '__main__':
    a=superman(deposit=1000,str=99,name='...',weight=100)
    a.speak()
    a.climb()