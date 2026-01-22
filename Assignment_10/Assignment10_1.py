# Write a program which accepts one number and prints the multiplication table of that number

def MultiplicationTable():
    i = 1
    while i in range(11):
        print(4 * i)
        i = i + 1

def main():
    MultiplicationTable()

if __name__ == "__main__":
    main()