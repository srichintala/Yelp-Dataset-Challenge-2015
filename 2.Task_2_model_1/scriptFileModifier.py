import csvModifier as cfile
import FeatureGenerator as feature
import FeatureSelection as FS
import PreProcessing as PreProc
import os

'''
Auhor : Aniket Gaikwad
Desc : This file will call the reading of Business_review.
      B ased on 'Flag' either 1 or 2 it will perform either generation of category list or new business_review file.
'''

def GenCat(dirPath):
    """
    Desc Part_1 : Generate Category or New Business_File with category splitting
    """
    flag=2
    o=cfile.csvHandler(dirPath)
    if(flag==1):
        file="yelp_academic_dataset_business.csv"
        o.readFile(file,1)
        o.writeFile('CategoryBusinessMapping.csv',1)
    elif(flag==2):
        file="yelp_academic_dataset_business.csv"
        o.readFile(file,2)
        o.writeFile('Business_File.csv',2)

def filterSplit(dirPath):
    """
    Desc : Filter & Split Reviews in Train and Test
    """
    oReview=cfile.ReviewTrainTestGenerator(dirPath)
    file="CategoryBusinessMapping.csv"
    oReview.fileReviewFile(file)
    ### Write Train File
    oReview.writeFile('Train_Review.csv',1)
    ### Write Test File
    oReview.writeFile('Test_Review.csv',2)

def featureGen():
    """
    Desc : Genarate Features
    """
    print('\n ********** Feature Generator ***********')
    fileName='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Train_Review.csv'
    mapFile='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Business_File.csv'
    writeFile='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Generated_Features.csv'
    oFeature=feature.featureGen()
    oFeature.getBusinesSToCato(mapFile)
    oFeature.generateFeature(fileName,writeFile)

def applyPreProc():
    """
    Desc : Apply Preprocessing
    """
    print('\n ********* Preprocessing **********')
    #fileName='/nobackup/anikgaik/search/features/Train_Features/Train_Features_Modified.csv'
    #writeFile='/nobackup/anikgaik/search/features/Train_Features/Train_Features_Replacing_Missing.csv'
    fileName='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Selected_Features.csv'
    writeFile1='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Train_Features_Modified.csv'
    writeFile2='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Final_Train_Features.csv'

    oPP=PreProc.preprocessing()
    oPP.removeFeature(fileName,writeFile1)
    oPP.featureDiscretization(writeFile1,writeFile2)


def featureSelect():
    """
    Desc : Feature Selection
    """
    print('\n ********** Feature Selector ***********')
    #fileName='/nobackup/anikgaik/search/features/Train_Features/Train_Features.csv'
    #writeFile='/nobackup/anikgaik/search/features/Train_Features/Final_train_Feature.csv'
    fileName='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Generated_Features.csv'
    writeFile='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Selected_Features.csv'
    oFS=FS.featureSelect()
    oFS.loadfeature(fileName)
    oFS.printAll()
    oFS.selectFeatures()
    oFS.generateNewfeature(fileName,writeFile)



if __name__=="__main__":
    """
    Desc : main function . Please comment or uncomment methods below to run required functions.
    """
    #dirPath="/nobackup/anikgaik/search/csv"
    dirPath="D:\\Fall 2015\\Search\\YELP Challenge\\Data"
    GenCat(dirPath)
    featureGen()
    featureSelect()
    applyPreProc()


