
import numpy as np
import math

def EucDistance(P1,P2):
    Ans = math.sqrt(((P1['X'] - P2['X'])** 2) + ((P1['Y'] - P2['Y'])** 2))
    return Ans


def MarvellousKNeighborsClassifier():
    Border = "-"*40
    data =[
            {'point':'A','X':1,'Y':2,'label': 'Red'},
            {'point':'B','X':2,'Y':3,'label': 'Red'},
            {'point':'C','X':3,'Y':1,'label': 'Blue'},
            {'point':'D','X':6,'Y':5,'label': 'Blue'}
           ]
    
    print(Border)
    print("Marvellous UserDefined KNN")
    print(Border)

    print(Border)
    print("Training Data Set")
    print(Border)

    for i in data:
        print(i)

    print(Border)

    new_point = {'X':int(input("Enter coordinate for X : ")),'Y':int(input("Enter Coordinate for Y : "))}

    #CALCULATE ALL DISTANCE 

    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(Border)
    print("Calculated Distance are :")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data,key= lambda item : item['distance'])

    print(Border)
    print("Sorted Data is :")
    print(Border)

    for d in sorted_data:
        print(d)

    K = 3
    nearest = sorted_data[:K]

    print(Border)
    print("Nearest 3 Elements are :")
    print(Border)

    for d in nearest:
        print(d)

    #VOTING

    Votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        Votes[label] = Votes.get(label,0) + 1

    print(Border)
    print("Voting Result is :")
    print(Border)

    for d in Votes:
        print("Name :",d,"Number of Votes :",Votes[d])

    print(Border)

    predicted_class = max(Votes,key=Votes.get)

    print("Predicted Class of (3,3) is :",predicted_class)

    print(Border)

def main():
    MarvellousKNeighborsClassifier()
    
if __name__=="__main__":
    main()