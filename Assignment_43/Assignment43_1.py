from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def MarvellousClassifier(Datapath):
    border = "--"*40
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
    # STEP 2 : SEPERATE INDEPENDENT AND DEPENDENT VARIABLES
    #--------------------------------------

    print(border)
    print("STEP 2 : SEPERATE INDEPENDENT AND DEPENDENT VARIABLES")
    print(border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("SHAPE OF X :",X.shape)
    print("SHAPE OF Y :",Y.shape)

    print(border)
    print("INPUT COLUMNS :",X.columns.to_list())
    print("OUTPUT COLUMN : Play")
    print(border)

    #--------------------------------------
    # STEP 3 : SPLIT THE DATASET FOR TRAINING AND TESTING
    #--------------------------------------

    print(border)
    print("STEP 3 : SPLIT THE DATASET FOR TRAINING AND TESTING")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print(border)
    print("INFORMATION OF TRAIINING AND TESTING DATA")
    print("X_TRAIN SHAPE :",X_train.shape)
    print("X_TEST SHAPE :",X_test.shape)
    print("Y_TRAIN SHAPE :",Y_train.shape)
    print("Y_TEST SHAPE :",Y_test.shape)
    print(border)
    
    #--------------------------------------
    # STEP 4 : ENCODING
    #--------------------------------------

    print(border)
    print("STEP 4 : ENCODING")
    print(border)

    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    X_train['Whether'] = le_weather.fit_transform(X_train['Whether'])
    X_train['Temperature'] = le_temp.fit_transform(X_train['Temperature'])

    X_test['Whether'] = le_weather.transform(X_test['Whether'])
    X_test['Temperature'] = le_temp.transform(X_test['Temperature'])

    Y_train = le_play.fit_transform(Y_train)
    Y_test = le_play.transform(Y_test)
    
    #--------------------------------------
    # STEP 5 : TESTING THE DATA
    #--------------------------------------

    print(border)
    print("STEP 5 : TESTING THE DATA")
    print(border)
    
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    Check_Accuracy = accuracy_score(Y_test,Y_pred)
    print("ACCURACY OF MODEL IS :",Check_Accuracy * 100)


def main():
    border = "-"*40

    print(border)
    print("PLAY PREDICTOR USING KNN")
    print(border)

    MarvellousClassifier("PlayPredictor.csv")


if __name__=="__main__":
    main()

