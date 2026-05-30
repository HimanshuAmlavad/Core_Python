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

class Rectangle(Shape):

    def __init__(self):
        self.length = 0
        self.width = 0

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width


s = Rectangle()
s.set_color('red')
s.set_border_width(2.5)
s.set_length(23)
s.set_width(90)

print('Shape color:',s.get_color())
print('Shape border width: ',s.get_border_width())
print('Rectangle length: ',s.get_length())
print('Rectangle width: ',s.get_width())