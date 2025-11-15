class programer:  
    company = 'Microsoft'
    salary = "120000"
    def __init__(self,company,skill,salary):
        self.company = company
        self.salary = salary
        self.skill = skill  # Dunder method are automatically called  # init call ho jaye ga jab ap ek object baye ge
   
divyanshu = programer('microsoft','advance dsa',1500000)

