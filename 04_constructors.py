class employee:  
    language = 'py' #class attribute
    salary = '1000' #class attribute

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language  # Dunder method are automatically called  # init call ho jaye ga jab ap ek object baye ge
        print('I am creating an object')
      
harry = employee('harry','1200000','javascrript') #  it is compulsary to pass three values
harry.name = 'Devid'
print(harry.name,harry.salary,harry.language,)






















