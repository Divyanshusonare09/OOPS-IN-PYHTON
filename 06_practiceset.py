# write a class calculator capable for finding squareroot cube and square of the number 

class calculator():
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f'the square of the number is {self.n*self.n}')
    def square_root(self):
        print(f'the square root of the number os {self.n**1/2}')


a = calculator(4)
a.square()
a.square_root()