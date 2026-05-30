class Shape:
    'This is a shape class'
    def __init__(self):
        self.border_width = 0
        self.color = ''

    def set_border_width(self, border_width):
        self.border_width = border_width

    def get_border_width(self):
        return self.border_width

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __del__(self):
        class_name = self.__class__.__name__
        print("Destroying class :", class_name)

    def __str__(self):
        return "This is the Constructor of class Shape"

s = Shape()
s.set_color('red')
s.set_border_width(2.5)

print('Shape color:',s.get_color())
print('Shape border width: ',s.get_border_width())
print(s)
print('shape doc: ',s.__doc__)
classes = s.__class__
print('Class name', classes.__name__)
print('module: ',s.__module__)
#print('Bases: ', s.__bases__)
print('Dict:', s.__dict__)
