# Write a program which accepts one character and checks whether it is a vowel or consonant
def Alphabet():
    Character = input("Enter Alphabet : ")[0]

    if Character in "A""a""E""e""I""i""O""o""U""u" : 
        print(Character,"is a Vowel")
    else:
        print(Character,"is a Consonant")

def main():
    Alphabet()

if __name__=="__main__":
    main()