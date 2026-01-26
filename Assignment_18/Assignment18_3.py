# Write a program which accepts N number from user and store it into list
# # Return Minimum of all elements from that list

def main():
    No = int(input("Enter Count : "))

    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)

    Min = Numbers [0]

    for num in Numbers:
        if num < Min:
            Max = num 

    print(Min)

if __name__=="__main__":
    main()