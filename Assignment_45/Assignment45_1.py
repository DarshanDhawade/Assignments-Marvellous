from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd


def MarvellousClassifier(Datapath):
    border = "-"*40
    #--------------------------------------
    #STEP 1 : LOAD THE DATASET
    #--------------------------------------

    print(border)
    print("STEP 1 : LOAD THE DATASET FROM CSV FILE")
    print(border)

    df=pd.read_csv(Datapath)
    print(border)
    print("SOME ENTRIES FROM THE DATASET")
    print(df.head)
    print(border)

    #--------------------------------------
    # STEP 2 : CLEAN THE DATASET BY REMOVING EMPTY ROWS
    #--------------------------------------

    print(border)
    print("STEP 2 : CLEAN THE DATASET BY REMOVING EMPTY ROWS")
    print(border)
    
    df.dropna(inplace=True)
    print("TOTAL RECORS :",df.shape[0])
    print("TOTAL COLUMNS :",df.shape[1])
    print(border)

    #--------------------------------------
    # STEP 3 : SEPERATE INDEPENDENT AND DEPENDENT VARIABLES
    #--------------------------------------

    print(border)
    print("STEP 3 : SEPERATE INDEPENDENT AND DEPENDENT VARIABLES")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("SHAPE OF X :",X.shape)
    print("SHAPE OF Y :",Y.shape)

    print(border)
    print("INPUT COLUMNS :",X.columns.to_list())
    print("OUTPUT COLUMN : Class")
    print(border)

    #--------------------------------------
    # STEP 4 : SPLIT THE DATASET FOR TRAINING AND TESTING
    #--------------------------------------

    print(border)
    print("STEP 4 : SPLIT THE DATASET FOR TRAINING AND TESTING")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("INFORMATION OF TRAIINING AND TESTING DATA")
    print("X_TRAIN SHAPE :",X_train.shape)
    print("X_TEST SHAPE :",X_test.shape)
    print("Y_TRAIN SHAPE :",Y_train.shape)
    print("Y_TEST SHAPE :",Y_test.shape)
    print(border)
    
    #--------------------------------------
    # STEP 5 : TRAIN AND TEST THE MODEL
    #--------------------------------------

    print(border)
    print("STEP 5 : TRAIN AND TEST THE MODEL")
    print(border)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    Accuracy = accuracy_score(Y_test,Y_pred)
    print("ACCURACY OF THE MODEL IS :",Accuracy*100)
    
def main():
    border = "-"*40

    print(border)
    print("WINE CLASSIFIER USING KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")


if __name__=="__main__":
    main()