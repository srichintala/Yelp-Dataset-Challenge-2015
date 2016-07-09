import csv
import collections
import itertools
import sys

csv.field_size_limit(sys.maxsize)

class csvHandler:
    """
    This class has methods that handles the CSV file operations
    """
    def __init__(self,dirName):
        self.dirName=dirName
        #self.fileName=None
        self.listOfbusiness=None
        self.data=None

    def readFile(self,fileName,flag):
        """
        This function will read file and update the list of list that can be written to new file.
        Flag = 1 Generate the Category : [business_id]
        Flag = 2 Genarate the splitted Category list
        """
        fileName=self.dirName+"\\"+fileName
        fr=csv.reader(open(fileName,"r"))
        firstline=True
        rowCnt=0
        bad_chars='[]"'''


        if flag==1:
            categoryDict=collections.defaultdict(list)


            for row in fr:
                if firstline:
                    firstline=False
                    continue
                else:
                    # row[9] -- Category
                    # row[16] -- business
                    rowCnt+=1
                    categorylist=row[9]
                    #print("CategoryList : {0}").format(categorylist)
                    ## Remove the []
                    for c in bad_chars:categorylist=categorylist.replace(c," ")
                    categorylist=categorylist.split(",")
                    businessid=row[16]
                    for category in categorylist:
                        category=category.replace(" ","")
                        #print('\n Category : {0}').format(category)
                        if categoryDict.has_key(category):
                            categoryDict[category].append(businessid)
                        else:
                            categoryDict[category]=[businessid]
                            #print('\n category : {0}').format(category)
            listOfCategory=[]
            for key,value in categoryDict.iteritems():
                value=map(str,value)
                value=",".join(value)
                value=value.replace('"',"")
                #print('\n value : {0}').format(value)
                temp=[key,value]
                listOfCategory.append(temp)
                #if(key=="'Restaurants'"):
                    #print('\n Key : {0} Value : {1}').format(key,value)
            self.listOfbusiness=listOfCategory


        elif flag==2:
            print('\n Flag_2 :')
            categoryCnt=0
            print('\n Finding distinct categories : ')
            categoryDict={}
            for row in fr:
                if firstline:
                    firstline=False
                    continue
                else:
                    # row[9] -- Category
                    rowCnt+=1
                    categorylist=row[9]
                    for c in bad_chars:categorylist=categorylist.replace(c,'')
                    categorylist=categorylist.split(",")
                    for category in categorylist:
                        category=category.replace(" ","")
                        category=category.replace("'","")
                        category=category.lower()
                        #category=category.stripe()
                        #if(category.lower()=='Restaurants'.lower()):
                            #print('\n Category : {0}').format(category)
                        if category in categoryDict:
                            continue
                        else:
                            categoryCnt+=1
                            categoryDict[category]=0
                            #print('\n Category : {0}').format(category)
            #print('\n Total number of categories : {0}').format(categoryCnt)
            listOfCategory=[]
            for key,value in categoryDict.iteritems():
                listOfCategory.append(key)
            #print('\n listOfCategory : {0}').format(listOfCategory)

            fr=csv.reader(open(fileName,"rb"))
            print('\n Building string to write :')
            newListToWrite=[]
            firstline=True
            for row in fr:
                newRow=[]
                if firstline:
                    firstline=False

                    for x in row:
                        x=x.replace(" ","")
                        x=x.replace("'","")
                        x=x.lower()
                        newRow.append(x)

                    newRow.extend(listOfCategory)
                    newListToWrite.append(newRow)
                    #print('\n newListToWrite : {0}').format(row)
                    continue
                else:
                    categorylist=row[9]
                    for c in bad_chars:categorylist=categorylist.replace(c,'')
                    catlist=categorylist.split(",")
                    categorylist=[]
                    #print('\n categorylist : {0}').format(categorylist)
                    for category in catlist:
                        category=category.replace(" ",'')
                        category=category.replace("'","")
                        category=category.lower()
                        categorylist.append(category)

                    d = dict.fromkeys(categorylist)
                    #print('\n d : {0}').format(d)
                    tempCat=[]
                    for category in listOfCategory:
                        category=category.replace(" ",'')
                        category=category.replace("'","")
                        category=category.lower()
                        if category in d:
                            #print('\n *************** Hit ********************')
                            tempCat.append('1')
                        else:
                            tempCat.append('0')
                    newRow.extend(row)
                    newRow.extend(tempCat)
                    newListToWrite.append(newRow)
                    #print('\n newListToWrite : {0}').format(newListToWrite)
            self.data=newListToWrite
            #print('\n To be written : {0}').format(self.data)

        else:
            print('\n ******** ERROR *************')
            print('\n Wrong Flag')

    def writeFile(self,fileName,flag):
        print('\n Writting starts : ')
        #fileName=self.dirName+"/"+fileName
        fileName=fileName
        with open(fileName, 'wb') as fp:
            a = csv.writer(fp, delimiter=',')

            if flag==1:
                a.writerows(self.listOfbusiness)
            elif flag==2:
                a.writerows(self.data)
            else:
                print('\n ******** ERROR *************')
                print('\n Wrong Flag')


class ReviewTrainTestGenerator:
    """
    This class has methods that will generate features.
    """
    def __init__(self,dirName):
        self.dirName=dirName
        #self.fileName=None
        self.listOfbusiness=None
        self.testData=None
        self.trainData=None
        self.data=None


    def fileReviewFile(self,categoryMapFile):
        fr=csv.reader(open(categoryMapFile,"r"))
        listOfBusiness=[]
        for row in fr:
                category=row[0].lower()
                if(category=="'restaurants'"):
                    print('\n Category : {0}').format(category)
                    listOfBusiness.extend(row[1].split(','))
                    #print('\n Business : {0}').format(listOfBusiness)

        # Convert List of Restaurant business to Dictionary
        dictOfRestaurants = dict.fromkeys(listOfBusiness)

        # For each review in review file filter the restaurants business and
        # its ratings.
        reviewFile=self.dirName+"\\"+'yelp_academic_dataset_review.csv'
        reviewfr=csv.reader(open(reviewFile,"r"))
        countOfreview=0
        newReviewList=[]
        firstline=True
        headerForFile=[]
        for review in reviewfr:
            if firstline:
                firstline=False
                headerForFile.extend(review)
                print('\n Header : {0}').format(headerForFile)
                continue
            if(dictOfRestaurants.has_key(review[4])):
                countOfreview+=1
                #print('\n Business_id : {0} , Rating : {1}').format(review[4],review[-4])
                newReviewList.append(review)

        # For Filtered Reviews (total = 9,90,627), create the test and train file
        print('\n Total Review Considered : {0}').format(countOfreview)
        trainCount=0
        trainData=[]
        testData=[]
        testCount=0
        firstTrain=True
        firstTest=True
        for review in newReviewList:
            if(trainCount<=(countOfreview*0.66)):
                if(firstTrain):
                    trainData.append(headerForFile)
                    firstTrain=False
                trainCount+=1
                trainData.append(review)
            else:
                if(firstTest):
                    testData.append(headerForFile)
                    firstTest=False
                testCount+=1
                testData.append(review)
        self.trainData=trainData
        self.testData=testData
        print('\n TrainCount : {0} , TestCount : {1}').format(trainCount,testCount)


    def writeFile(self,fileName,flag):
        print('\n Writting starts : ')
        #fileName=self.dirName+"/"+fileName
        if flag==1:
            # Write Train File
            fileName=fileName
            self.data=self.trainData
        elif flag==2:
            # Write Test File
            fileName=fileName
            self.data=self.testData
        else:
            print('\n ******** ERROR *************')
            print('\n Wrong Flag')
        #print('\n Data : {0}').format(self.data)
        with open(fileName, 'wb') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(self.data)











