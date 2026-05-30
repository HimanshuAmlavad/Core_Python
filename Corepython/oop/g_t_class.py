class Exercise:

    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0

    def set_num1(self, n):
        self.__num1 = n

    def get_num1(self):
        return self.__num1

    def set_num2(self, n):
        self.__num2 = n

    def get_num2(self):
        return self.__num2

    def sum(self):
        c = self.get_num1() + self.get_num2()
        print('sum:', c)

class Alphabat:

    def __init__(self):
        self.__name = ''

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def alphabat_count(self):

        count = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            count = 0
            for j in self.get_name():
                if i == j:
                    count += 1
            if count > 0:
                print(i, "=", count)

class number_triangle:

    def __init__(self):
        self.row = 0
        self.col = 0

    def set_row_col(self, num):
        self.row = num
        self.col = num

    def get_row_col(self):
        return self.row , self.col

    def triangle(self):
        def triangle_pattern(num):
            row = num
            col = num

            for r in range(1, row + 1):
                for c in range(1, r + 1):
                    print(c, end='\t')
                print()

a = number_triangle()
a.set_row_col(5)
a.triangle()