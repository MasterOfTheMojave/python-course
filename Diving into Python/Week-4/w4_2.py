class Value:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __set__(self, obj, value):
        obj.__dict__[self.name] =  int(value - value * obj.__dict__['commission'])
    
    def __get__(self, obj, owner):
        return obj.__dict__[self.name]

class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission