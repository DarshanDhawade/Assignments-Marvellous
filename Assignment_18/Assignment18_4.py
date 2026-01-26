# Write a program which accepts N number from user and store it into list
# # Accept one another number from user and return frequency of that number from list 

def main():
    No = int(input("Enter Count : "))

    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)

    Frequency = {}

    for num in Numbers:
        if num in Frequency:
            Frequency[num] += 1
        else:
            Frequency[num] = 1

    Max_Freq = 0
    Max_Element = None

    for x in Frequency:
        if Frequency[x] > Max_Freq:
            Max_Freq = Frequency[x]
            Max_Element = x

    print("Element with highest frequency : " , Max_Element)

if __name__=="__main__":
    main()