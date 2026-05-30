class Math:

    def sum(self,a,b,c):
        print('sum of two number: ', a+b+c)


class Add(Math):

    def sum(self,a,b):
        print('Sum of three number: ',a+b)


r = Math()
r.sum(2,2,2)

s = Add()
s.sum(2,2)

shape:Math = Add()
shape.sum(3,3)