# Write a program which accepts N number from user and store it into list
# # Return Maximum of all elements from that list

def main():
    No = int(input("Enter Count : "))

    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)

    Max = 0

    for num in Numbers:
        if num > Max:
            Max = num 

    print(Max)

if __name__=="__main__":
    main()