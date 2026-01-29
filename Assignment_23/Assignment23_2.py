# Write a python program to implement a class named BankAccount with the following requirements

class BankAccount:
    ROI = 10.5
    
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
        
    
    def Display(self):
        print("Account Holder : ",self.Name)
        print("Cutrent Balance : ",self.Amount)

    def Deposit(self,amount):
        self.Amount += amount
        print("Deposited : ",amount)
        print("updated balance : ",self.Amount)

    def Withdraw(self,amount):
        if amount <= self.Amount:
            self.Amount -= amount
            print("Withdrawn : ",amount)
            print("Remaining Balance : ",self.Amount)
        else:
            print("Insufficient Balance")


    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


obj1 = BankAccount("Rahul",100000)
obj1.Display()
obj1.Deposit(25000)
obj1.Withdraw(50000)

print("--"*100)

obj2 = BankAccount("Vikas",500000)
obj2.Display()
obj1.Deposit(150000)
obj1.Withdraw(10000)

