class Person:

    def __init__(self):
        self.name = ''
        self.address = ''
        self.age = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


p = Person()
p.set_name('himanshu')
p.set_address('ujjain')
p.set_age(25)

print(p.get_name())
print(p.get_address())
print(p.get_age())