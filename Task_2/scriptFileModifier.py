import csvModifier as cfile
import FeatureGenerator as feature
import os

'''
This file will call the reading of Business_review.
Based on 'Flag' either 1 or 2 it will perform either generation of category list or new business_review file.
'''

if __name__=="__main__":
    #dirPath="/nobackup/anikgaik/search/csv"
    dirPath="D:\\Fall 2015\\Search\\YELP Challenge\\Data"
    '''
    flag=2
    o=cfile.csvHandler(dirPath)
    if(flag==1):
        file="yelp_academic_dataset_business.csv"
        o.readFile(file,1)
        o.writeFile('CategoryBusinessMapping.csv',1)
    elif(flag==2):
        file="yelp_academic_dataset_business.csv"
        o.readFile(file,2)
        o.writeFile('newBusinessFile.csv',2)

    oReview=cfile.ReviewTrainTestGenerator(dirPath)
    file="CategoryBusinessMapping.csv"
    oReview.fileReviewFile(file)
    ### Write Train File
    oReview.writeFile('Train_Review.csv',1)
    ### Write Test File
    oReview.writeFile('Test_Review.csv',2)
    '''


    fileName='Train_Review.csv'
    mapFile='newBusinessFile.csv'
    writeFile='Train_Features.csv'
    oFeature=feature.featureGen()
    oFeature.getBusinesSToCato(mapFile)
    oFeature.generateFeature(fileName)
    oFeature.writeFile(writeFile)


