class my_error(Exception):
    
    def __init__(self,value):
        self.value = value
    
    def __str__(self) -> str:
        return (repr(self.value))


try:
    raise my_error('mera exception')
except my_error as e:
    print('new exception has occured',e.value)