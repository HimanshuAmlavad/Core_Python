class Person:
    company = 'Rays EdTech'

    def __init__(self):
        print('i am constructor')
        self.name = 'himanshu'
        self.address = 'ujjain'

    def get_name(self):
        print('my name is himanshu')

    @classmethod
    def get_test(self):
        print('test method')


p = Person()
# p.get_name()
# Person.get_test()
# p.get_test()
print(p.name, p.address)
