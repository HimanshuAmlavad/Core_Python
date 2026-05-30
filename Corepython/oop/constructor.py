class Shape:
    count = 0 # class variable {it can be directly initilise by class name. it has static memory, dosen't matter how many times u call the class or any method}

    #def __init__(self):  # non-parametarise constructor
    #    self.color = ''
     #   self.border_width = 0

    #def __init__(self): #simple emmition of default constructor
    #    pass

    def __init__(self, color='', border_width=0): # parameterise constructor with default value
        self.color = color # instance variable { it is initilise by constructor. it always get new memory location when new object is created}
        self.border_width = border_width # instance variable

    def set_color(self, color): # instance method , color: local variable
        self.color = color

    def get_color(self):
        return self.color

    def set_border_width(self, border_width):
        self.border_width = border_width

    def get_border_width(self):
        return self.border_width

    def area(self):
        print('shape class area method')

s = Shape('red', 200) # object created and pass the argument for the constructor to initilize the value ( direct inilization, fast)

print(s.get_color(), s.get_border_width())

s.color = 'aaa' # initilized variable, directly using object (not applicable for pricvate or protected)
s.border_width = 10
print(s.get_color(), s.get_border_width())

s.set_color('bbb')  #initilizing instance varible via setter method
s.set_border_width(20)
print(s.get_color(), s.get_border_width())
