import  numpy as np
import csv
import algorithms as algs
import DataVisualization as DV
import  pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
from operator import itemgetter
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from sklearn.cross_validation import KFold
from sklearn.metrics import r2_score



"""
Name :  Aniket Gaikwad
description : Main Method.
"""

def writeToFile(data,fileName):
    """

    Args:
        data: Dataset
        fileName: Outfile

    Returns: None

    """
        #print('\n Writting File {0} : ').format(fileName)
        #fileName=self.dirName+"/"+fileName
        with open(fileName, 'ab') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(data)

def featureSelection(X,Y):
    """
    Desc : Apply feature selection like VarianceThreshold,Select K best
    Args:
        X: Train Data
        Y: Label

    Returns: Modified traindata

    """
    sel = VarianceThreshold(threshold=(.9 * (1 - .9)))
    x=sel.fit_transform(X)
    print('\n Size of dataset after removing variance: {0}').format(x.shape)
    model=SelectKBest(chi2,k=100)
    dataset=model.fit_transform(X,Y)
    print('\n Size of dataset after selcting K Best: {0}').format(dataset.shape)
    return(dataset)

def beliefNet(trainset,testset):
    """
    Desc : Application of belief network
    Args:
        trainset: Train data
        testset: Test data

    Returns: Modified train and test data

    """
    ## Deep Belief Network
    print('\n Using Belief Network')
    beliefNet=algs.DeepBeliefNetwork(1000,learning_rate=0.1)
    beliefNet.learn(trainset[0], trainset[1])
    newTrain=beliefNet.transform(trainset[0])
    #trainset[0]=newTrain
    print('\n size of train dataset after belief Net : {0}').format(newTrain.shape)
    #newTrain=None
    newTest=beliefNet.transform(testset[0])
    #testset[0]=newTest
    print('\n size of test dataset after belief Net : {0}').format(newTest.shape)
    #newTest=None
    return ((newTrain,trainset[1]),(newTest,testset[1]))
    #####################


def ApplyPCA(X):
    """
    Desc : PCA transformation of data
    Args:
        X: TrainData

    Returns: TransformedData

    """
    #numinputs=dataset.shape[1]-1
    #X=dataset[:,0:numinputs]

    pca=PCA(n_components=15)
    pca.fit(X)
    print(pca.explained_variance_ratio_)
    print('\n Sum : {0}').format(sum(pca.explained_variance_ratio_))
    newX=pca.transform(X)
    return newX

def getSplitNew(train,test):
    print('\n Split the dataset ....')
    numinputs=train.shape[1]-1
    Xtrain=train[:,0:numinputs]
    Ytrain=train[:,numinputs]
    Xtest=test[:,0:numinputs]
    Ytest=test[:,numinputs]

    return((Xtrain,Ytrain),(Xtest,Ytest))


def splitdataset(dataset,trainsize=7000,testsize=3000,testfile=None):
    """
    Desc : Sample train data and test data.
    Args:
        dataset: Dataset
        trainsize: trainsize
        testsize: testsize
        testfile: testFile if any

    Returns: Train and test sample data

    """
    print('\n Split the dataset ....')

    #####
    ### Full data use for validation
    #s=dataset.shape[0]
    #trainsize=int(s*0.66)
    #testsize=int(s*0.34)
    #print('\n Size : {0} , train : {1} test : {2} ').format(s,,)
    #####
    randindices=np.random.randint(0,dataset.shape[0],trainsize+testsize)

    numinputs=dataset.shape[1]-1
    Xtrain=dataset[randindices[0:trainsize],0:numinputs]
    Ytrain=dataset[randindices[0:trainsize],numinputs]
    Xtest=dataset[randindices[trainsize:trainsize+testsize],0:numinputs]
    Ytest=dataset[randindices[trainsize:trainsize+testsize],numinputs]

    #################
    '''
    enc = OneHotEncoder()
    enc.fit(Xtrain)
    Xtrain=enc.transform(Xtrain).toarray()
    Xtest=enc.transform(Xtest).toarray()
    '''
    ################
    if testfile is not None:
        testdataset=loadcsv(testfile)
        Xtest=dataset[:,0:numinputs]
        Ytest=dataset[:,numinputs]

    return((Xtrain,Ytrain),(Xtest,Ytest))

def loadcsv(fileName):
    """
    File loading function for model_1
    Args:
        fileName:

    Returns: Dataset
    """
    dataframe=pd.read_csv(fileName,delimiter=',')
    #dataset=np.loadtxt(fileName,delimiter=',',dtype=None)
    #dataset=np.genfromtxt(fileName,delimiter=',')
    # 8th column is class label
    #dataset=dataframe.as_matrix()
    dataset=dataframe.values
    dataset=dataset[:,2:-1]
    dataset[:,[6,-1]]=dataset[:,[-1,6]]
    return dataset

def loadcsv_sentiment(fileName):
    """

    File loading function for model_2
    Args:
        fileName:

    Returns: Dataset

    """
    dataframe=pd.read_csv(fileName,delimiter=',')
    dataset=dataframe.values
    return dataset

def loadDataSenti(fileName):
    """
    File loading function for model_2
    Args:
        fileName:

    Returns: Dataset

    """
    dataset=None
    print('\n Loading data .....')
    dataset=loadcsv_sentiment(fileName)
    print('\n Size of data : {0}').format(dataset.shape)
    dataset=dataset.astype(int)
    return dataset


def loadData(fileName):
    """
    Desc : Load data, encode data using one-hot encoder, perform feature selection
    Args:
        fileName: FileName

    Returns: Dataset

    """
    dataset=None
    print('\n Loading data .....')
    dataset=loadcsv(fileName)
    print('\n Size of data : {0}').format(dataset.shape)
    dataset=dataset.astype(int)

    ### Sepearate the label and features
    numinputs=dataset.shape[1]-1
    Xdataset=dataset[:,0:numinputs]
    Ydataset=dataset[:,numinputs:]
    #print('\n Ydataset : {0}').format(Ydataset)
    ####################
    print('\n Dataset Transform Starts ........')
    enc = OneHotEncoder()
    enc.fit(Xdataset)
    dataset=enc.transform(Xdataset).toarray()
    #print('\n Size after OneHotEncoder : {0}').format(dataset.shape)
    #dataset[:,-1]=Ydataset
    ########### Feature selection
    dataset=featureSelection(dataset,Ydataset)
    print('\n Size of dataset : {0}').format(dataset.shape)
    ########## PCA
    #dataset=ApplyPCA(dataset)
    dataset=np.append(dataset,Ydataset,axis=1)
    #print('\n dataset : {0}').format(dataset)
    ######## Data Visualization
    #dataViz=DV.Visualization()
    #dataViz.visualization_2d(dataset)
    ####### 3-D Visualization
    #dataViz.visualization_3d(dataset)
    return dataset


def getSplit(dataset):
    """

    Args:
        dataset: Dataset

    Returns: trainset, testset

    """

    #################
    print('\n Dataset split starts ...........')
    trainset,testset=splitdataset(dataset)
    return trainset,testset

def getAccuracy(Ytest,predictions):
    """

    Args:
        Ytest: True Label
        predictions:  Predicted Label

    Returns: Accuracy

    """
    print('\n Calculating Accuracy.....')
    correct = 0
    for i in range(len(Ytest)):
        #print('\n YTest : {0} , predictions : {0}').format(Ytest[i],predictions[i])
        predictions[i]=roundOf(predictions[i])
        #print('\n Prediction : {0}').format(x)
        #print('\n Actual Value  : {0}').format(Ytest[i])
        if Ytest[i] == predictions[i]:
            correct += 1
    #print('\n Number of correct : {0}').format(correct)
    ######################
    result=map(list,zip(predictions,Ytest))
    writeToFile(result,'result.csv')
    #####################
    return (correct/float(len(Ytest))) * 100.0

def roundOf(x):
    """

    Args:
        x: float Value

    Returns: binned value

    """
    if(x >0.5 and x <=1.5):
        x=1
    elif(x>1.5 and x <=2.5):
        x=2
    elif(x>2.5 and x<=3.5):
        x=3
    elif(x>3.5 and x<=4.5):
        x=4
    else:
        x=5
    return x

def modifiedAccuracy(Ytest,predictions):
    """

    Args:
        Ytest: True Label
        predictions:  Predicted Label

    Returns: Hueristic Accuracy

    """
    print('\n Calculating Accuracy.....')
    correct = 0
    for i in range(len(Ytest)):
        #print('\n YTest : {0} , predictions : {0}').format(Ytest[i],predictions[i])
        if Ytest[i] == predictions[i]:
            correct += 1
        elif abs(Ytest[i]-predictions[i])<=1:
            correct+=0.90
        elif abs(Ytest[i]-predictions[i])>=1 and abs(Ytest[i]-predictions[i])<=2:
            correct+=0.5
        else:
            correct+=0

    #print('\n Number of correct : {0}').format(correct)
    ######################
    result=map(list,zip(predictions,Ytest))
    writeToFile(result,'result.csv')
    #####################
    return (correct/float(len(Ytest))) * 100.0


def RMSE_Evaluation(Ytest,predictions):
    """

     Args:
        Ytest: True Label
        predictions:  Predicted Label

    Returns: RMSE score

    """
    print('\n RMSE Evaluation : ')
    #print('\n Ytest : {0}').format(Ytest)
    #print('\n predictions : {0}').format(predictions)
    rms = sqrt(mean_squared_error(Ytest, predictions))
    return rms

def r_square_Evaluation(Ytest,predictions):
    """

    Args:
        Ytest: True Label
        predictions:  Predicted Label

    Returns: R2 score

    """
    print('\n RMSE Evaluation : ')
    #print('\n Ytest : {0}').format(Ytest)
    #print('\n predictions : {0}').format(predictions)
    r=r2_score(Ytest, predictions)
    return r




def getMaxAccuracyFeatures(accuracyList):
    """

    Args:
        accuracyList: List of accuracy

    Returns: max accuracy entry

    """
    return  max(accuracyList,key=itemgetter(0))[1]

def getClassLabelDistribution(fileName):
    """
    Desc : Plot Histogram for class labels
    Args:
        fileName: TrainFile

    """
    dataset=loadData(fileName)
    Label=dataset[:,-1]
    Label=Label.astype(int)
    print('Label : {0}').format(np.histogram(Label,bins=[1,2,3,4,5,6]))
    plt.hist(Label)
    plt.show()

def KfoldCrossValidation(dataset):
    """

    Args:
        dataset: Traindata

    Returns: Index of 10 folds

    """
    kf = KFold(dataset.shape[0],n_folds=10)
    return kf

def runClassifier(trainFile,testFile=None,NO_OF_EXECUTION=1,flag=None):
    """
    Desc : K-fold cross validation followed by classifier executions.
           Display results 'Accuracy','RMSE score','R2-Score'
    Args:
        trainFile: trainfilePath
        testFile:  testFilePath
        NO_OF_EXECUTION: Number of executions (default=1)
        flag: Flag=1 -- Model_1 , Flag_2=2 -- Model_2

    Returns: None

    """
    if(flag==1):
        ### Business Features
        dataset=loadData(trainFile)
    else:
        ### Sentiment Features
        dataset=loadDataSenti(trainFile)
    print('\n Size of dataset after loading : {0}').format(dataset.shape)
    kf=KfoldCrossValidation(dataset)
    i=1
    for train_index, test_index in kf:
        ### For Each Fold
        print('\n For Fold : {0}').format(i)
        i=i+1
        #print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = dataset[train_index], dataset[test_index]

        print('\n Train : {0} \n Test : {1}').format(X_train.shape, X_test.shape)

        #trainset,testset=getSplit(dataset)

        trainset,testset=getSplitNew(X_train,X_test)
        #trainset,testset=beliefNet(trainset,testset)


        print('Running  on train={0} and test={1} samples').format(trainset[0].shape, testset[0].shape)

        #ForwardFeatureSelection(trainset[0], trainset[1],testset[0],testset[1])


        classalgs = {#'Random': algs.Classifier(),
                     'Naive Bayes': algs.NaiveBayes(),
                    'Logistic Regression' : algs.LogisticRegression(),
                     'GradientBoostingRegressor' : algs.GradientBoost(),
                     'SVM_rbf' :algs.SVM(),
                     'SVM_linear' :algs.SVM(),
                     'SVM_Sigmoid' :algs.SVM('sigmoid'),
                    'DecisionTreeRegressor' : algs.DecisionTreeReg(),
                    'DecisionTreeClassifier' : algs.DecisionTreeClassifier(),
                    'RandomForestRegressor' : algs.RandForest()
                     }
        for learnername, learner in classalgs.iteritems():
            print('Running learner = {0}').format(learnername)
            # Train model
            learner.learn(trainset[0], trainset[1])
            # Test model
            predictions = learner.predict(testset[0])
            #print('\n Predictions : {0}').format(predictions)
            accuracy = getAccuracy(testset[1], predictions)
            print 'Accuracy for ' + learnername + ': ' + str(accuracy)
            accuracy=RMSE_Evaluation(testset[1], predictions)
            print 'RMSE Error for ' + learnername + ': ' + str(accuracy)
            accuracy=r_square_Evaluation(testset[1], predictions)
            print 'R2 Score for ' + learnername + ': ' + str(accuracy)
            #accuracy=modifiedAccuracy(testset[1], predictions)

            #print 'Hueristic Accuracy for ' + learnername + ': ' + str(accuracy)

def runOnFullData(trainFile,testFile=None,NO_OF_EXECUTION=1,flag=None):
    """
    Desc : Run the all classifiers on full data based on model selected.
    Args:
        trainFile: trainfilePath
        testFile:  testFilePath
        NO_OF_EXECUTION: Number of executions (default=1)
        flag: Flag=1 -- Model_1 , Flag_2=2 -- Model_2

    Returns: None

    """
    if(flag==1):
        ### Business Features
        TrainDataset=loadData(trainFile)
        TestDataset=loadData(trainFile)
    else:
        ### Sentiment Features
        TrainDataset=loadDataSenti(trainFile)
        TestDataset=loadDataSenti(testFile)
    print('\n Train dataset after loading : {0}').format(TrainDataset.shape)
    print('\n Test dataset after loading : {0}').format(TestDataset.shape)
    No_Of_Cols=TrainDataset.shape[1]-1
    Xtrain=TrainDataset[:,0:No_Of_Cols]
    Ytrain=TrainDataset[:,No_Of_Cols]
    Xtest=TestDataset[:,0:No_Of_Cols]
    Ytest=TestDataset[:,No_Of_Cols]
    classalgs = {#'Random': algs.Classifier(),
                     'Naive Bayes': algs.NaiveBayes(),
                    'Logistic Regression' : algs.LogisticRegression(),
                     'GradientBoostingRegressor' : algs.GradientBoost(),
                     'SVM_rbf' :algs.SVM(),
                     'SVM_linear' :algs.SVM(),
                     'SVM_Sigmoid' :algs.SVM('sigmoid'),
                    'DecisionTreeRegressor' : algs.DecisionTreeReg(),
                    'DecisionTreeClassifier' : algs.DecisionTreeClassifier(),
                    'RandomForestRegressor' : algs.RandForest()
                     }
    for learnername, learner in classalgs.iteritems():
        print('Running learner = {0}').format(learnername)
        # Train model
        learner.learn(Xtrain, Ytrain)
        # Test model
        predictions = learner.predict(Xtest)
        #print('\n Predictions : {0}').format(predictions)
        accuracy = getAccuracy(Ytest, predictions)
        print 'Accuracy for ' + learnername + ': ' + str(accuracy)
        accuracy=RMSE_Evaluation(Ytest, predictions)
        print 'RMSE Error for ' + learnername + ': ' + str(accuracy)
        accuracy=r_square_Evaluation(Ytest, predictions)
        print 'R2 Score for ' + learnername + ': ' + str(accuracy)
        #accuracy=modifiedAccuracy(testset[1], predictions)

        #print 'Hueristic Accuracy for ' + learnername + ': ' + str(accuracy)



if __name__ == '__main__':
    """
    Desc : Main function. Flag=1 -- Model_1 , Flag_2=2 -- Model_2
    """
    flag=1
    if(flag==1):
        fileName1="D:\\Fall 2015\\Search\\YELP Challenge\\/" \
                "Yelp-Dataset-Challenge-2015\\Task_2\\xyz1.csv"
        fileName2=None
        #fileName='/N/u/anikgaik/BigRed2/search/Aniket_Train_Features.csv'
    else:
        #fileName="D:\\Fall 2015\\Search\\YELP Challenge\\/" \
        #        "Yelp-Dataset-Challenge-2015\\Task_2\\N.csv"
        #fileName='/N/dc2/scratch/anikgaik/Train.csv'
        fileName1="D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\FeaturesOutput\\BigramFeatures\\OutputTrainUniBi.csv"
        fileName2="D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\FeaturesOutput\\BigramFeatures\\OutputTestUniBi.csv"
        runOnFullData(fileName1,fileName2,flag)
    runClassifier(fileName1,fileName2,1,flag)
    #getClassLabelDistribution(fileName)
    #ApplyPCA()

