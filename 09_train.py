# 5.
# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint  
class train:
    def __init__(self,name,station,to,):
        self.name = name
        self.station = station
        self.to = to
    
    def ticket(self):
        print(f"Train ticket is book from {self.station} to {self.to}")
    def status(self):
        print(f"{self.name} express  100 sits are available ")
        print(f"{self.name} express  is Running on the time Under Indian Railway")
    
passanger = train('narmada','nagpur','delhi')  
passanger.ticket()
passanger.status()

