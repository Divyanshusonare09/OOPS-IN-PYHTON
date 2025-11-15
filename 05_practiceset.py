# create a class programer for storing information 
# of few programe working at the microsoft

class programer:
    company = 'microsoft'
    skill = 'advance DSA'
    salary = '1500000'

    def get_info(self):
        print(f'the company of te programer is {self.company} and the skill of the programer is {self.skill} and the salary  of the programer is {self.salary}')

divyanshu = programer()
divyanshu.get_info()
print(divyanshu.company,divyanshu.skill,divyanshu.salary)

vinod = programer()
print(vinod.company,vinod.skill,vinod.salary)