class employee():
    language = 'Python'
    salary = '120000'

    def getinfo(self): # jab bhe koe function baye to self de
        print(f"The language of the Client is {self.language}. The salary is {self.salary}")

    @staticmethod 
    def greet(): #this functon does not need any self parameter we use @staticmethod
        print(f'Good morning')
harry = employee()
harry.greet()
harry.getinfo()

