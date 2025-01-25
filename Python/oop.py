# class programmer:
#     def __init__(self,name,salery):
#         self.name=name
#         self.salery=salery
#     def getinfo(self):
#         print(f"my name is {self.name}, my slaery is {self.salery}")
# obj1=programmer("ammara",1300)
# obj1.getinfo()



# class calculator:
#     def __init__(self,num):
#         self.num=num
#     def square(self):
#         print(f"Square of the number is :{self.num*self.num}")
#     def cube(self):
#         print(f"cube of the number is :{self.num*self.num*self.num}")
#     def squareroot(self):
#         print(f"square root of the number is :{self.num*0.5}")
# obj1=calculator(4)
# obj1.square()
# obj1.cube()
# obj1.squareroot()



class train:
    Train1="Milat Express"
    Train2="Pakistan Express"
    withoutAC_tickets=100
    AC_tickets=50
    def __init__(self,name):
        self.name=name
    
    def booktickets(self,train,seat):
        print(f"Welcom to the {train}")
        print(f"{self.name}, Your Ticker is book")
        if(seat=="AC"):
            
            print(f"Your Seat no : AC {self.AC_tickets}")
            self.AC_tickets=self.AC_tickets-1
        else:
             
            #  print(f"Your Seat no : {self.withoutAC_tickets}")
             self.withoutAC_tickets=self.withoutAC_tickets-1
        
    def status(self):
        print(f"Available trains are : {self.Train1}, {self.Train2}, and tikets in both train are availble AC seats: {self.AC_tickets}, and without AC :{self.withoutAC_tickets} ")



obj1=train("Ammara")
obj1.booktickets("Milat Express","AC")
obj1.status()