# Write a python program to implement a class named Numbers with the following specifications 

class Numbers :
    
    def __init__(self):
        self.Value = int(input("Enter Number : "))
        

    def ChkPrime(self):
            if self.Value <= 1:
                return False
            for i in range(2,int(self.Value ** 0.5)+1 ):
                if self.Value % i == 0:
                    return False
                 
            return True
                
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum += 0
        if sum == self.Value:
             return True
        else :
             return False
                   
    def Factors(self):
        factors = []
        for i in range(1,self.Value+ 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        total = 0     
        for i in range(1,self.Value+ 1):
            if self.Value % i == 0:
                total += i   
        return total  

obj1 = Numbers()
print("Is Prime : ",obj1.ChkPrime())
print("Is perfect : ",obj1.ChkPerfect())
print("Factors are : ",obj1.Factors())
print("Sum of Factors is : ",obj1.SumFactors())

print("_"*50)

obj2 = Numbers()
print("Is Prime : ",obj2.ChkPrime())
print("Is perfect : ",obj2.ChkPerfect())
print("Factors are : ",obj2.Factors())
print("Sum of Factors is : ",obj2.SumFactors())

print("_"*50)
            
obj3 = Numbers()
print("Is Prime : ",obj3.ChkPrime())
print("Is perfect : ",obj3.ChkPerfect())
print("Factors are : ",obj3.Factors())
print("Sum of Factors is : ",obj3.SumFactors())