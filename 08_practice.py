#4.
#Add a static method in problem 2, to greet the user with hello.

class calculator():
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f'the square of the number is {self.n*self.n}')
    def square_root(self):
        print(f'the square root of the number os {self.n**1/2}')
    @staticmethod
    def greet():
        print('welcome chief')
        


a = calculator(4)
a.greet()
a.square()
a.square_root()



