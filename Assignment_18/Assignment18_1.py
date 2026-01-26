# Write a program which accepts N number from user and store it into list
# # Return addition of all elements from that list

def main():
    No = int(input("Number Count : "))

    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)

    Total = 0

    for num in Numbers:
        Total = Total + num
    print("Addition is : " , Total)

if __name__=="__main__":
    main()