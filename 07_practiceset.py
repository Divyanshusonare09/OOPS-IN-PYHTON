
# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class Demo:
    a = 4

O = Demo()
print(O.a) # this will fist serch for instance attribute and then prints the class attibute
O.a = 0 # instance attribute which take priferace over class attribute
print(O.a) # this will print the class attribute
print(Demo.a)  # this will simply print the class attribute













