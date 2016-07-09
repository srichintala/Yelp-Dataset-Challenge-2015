import csv

def checkNull(file):
    fr=csv.reader(open(file))
    firstLine=True
    for row in fr:
        if(firstLine):
            print('\n row : {0}').format(row)
            firstLine=False
        else:
            if(row[4]==''):
                print('\n Business_id : {0}').format(row[4])


def checkFeatureFile(file):
    fr=csv.reader(open(file))
    size=0
    firstRow=True
    rowcount=0
    for row in fr:

        if(firstRow):
            size=len(row)
            print('\n Expected size : {0}').format(size)
            firstRow=False
        else:
            rowcount+=1
            if(size!=len(row)):
                print('\n size : {0} , rownumber : {1}').format(len(row),rowcount)
                print('\n Row : {0}').format(row)
    print('\n Number of rows : {0}').format(rowcount)


def businessTest(fileName):
    firstRow=True
    tempDict={}
    fr=csv.reader(open(fileName,'r'))
    for row in fr:
        businessVect=[]
        print('\n Len of Business File entry : {0}').format(len(row))
        if(firstRow):
            firstRow=False
            temp=[]
            #for x in row:
                #temp.append([x])
            #writeFile(temp,'test.csv')
            continue
        else:
            temp=[]
            for x in row:
                temp.append([x])
            writeFile(temp,'test.csv')
            break


def getFeature(fileName):
    firstRow=True
    tempDict={}
    fr=csv.reader(open(fileName,'r'))
    for row in fr:
        businessVect=[]
        print('\n Len of Business File entry : {0}').format(len(row))
        if(firstRow):
            firstRow=False
            temp=[]
            print(row)
            for x in row:
                temp.append([x])
            writeFile(temp,'test.csv')
            break



def writeFile(data,fileName):
        #print('\n Writting File {0} : ').format(fileName)
        #fileName=self.dirName+"/"+fileName
        with open(fileName, 'ab') as fp:
            a = csv.writer(fp, delimiter=' ')
            a.writerows(data)

if __name__=="__main__":
    #dirPath="D:\\Fall 2015\\Search\\YELP Challenge\\Data"
    #file="yelp_academic_dataset_review.csv"
    #file=dirPath+"\\"+file
    #file='Train_Review.csv'
    #checkNull(file)
    #file="Train_Features"
    #checkFeatureFile(file)
    #mapFile='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Business_File.csv'
    #businessTest(mapFile)
    fileName='D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\Train_Features_Modified.csv'
    getFeature(fileName)
