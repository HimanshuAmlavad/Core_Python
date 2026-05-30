class Addition:
    def add(self, a, b):
        return a + b


class Multiplication:
    def mul(self, a, b):
        return a * b

class Derived(Addition, Multiplication):  # derived class inherits both addition and mutiplacation base class
    def divide(self, a, b):
        return a/b

m = Derived()

print('Add: ',m.add(23, 24))
print('Mul: ',m.mul(15, 15))
print('Divide: ',m.divide(50, 2))


