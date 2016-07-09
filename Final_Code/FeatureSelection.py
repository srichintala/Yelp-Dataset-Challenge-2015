import  numpy as np
import csv
#import pandas as pd

"""
Name :  Aniket Gaikwad
description : This file implements all Feature selection methods.
"""

class featureSelect:
    def __init__(self):
        self.colStat=None
        self.selectedfeatures=None

    def loadfeature(self,file):
        print('\n Load Feature data : ')
        fp=csv.reader(open(file,'rb'))
        firstRow=True
        data=[]
        rowCount=0
        headerLen=0
        for row in fp:
            if(headerLen!=0 and headerLen!=len(row)):
                print('\n For row : {0} Len : {1}').format(row,len(row))
                continue

            if(firstRow):
                header=row
                firstRow=False
                d=dict.fromkeys(row)
                self.colStat=[0]*len(header)
                headerLen=len(header)
                print('\n Len of header : {0}').format(headerLen)
            else:
                rowCount+=1
                if(rowCount>=10000):
                    self.getStat(data)
                    data=[]
                    rowCount=0
                    #break

                else:
                    data.append(row)
        self.getStat(data)



    def getStat(self,data):
        """
        Calculate statistic of the dataset and store it future use.
        Args:
            data: Datatset

        Returns: None

        """
        #print('\n Get Stats of Data : ')
        for entry in data:
            for i in range(len(entry)):
                #print(entry[-1])
                if(entry[i]is 0 or entry[i]is '' or entry[i]is "0"):
                    self.colStat[i]=self.colStat[i]+1

    def selectFeatures(self):
        """
        Desc : Select the features that have < 6,40,000 zeros
        """
        l=[]
        for i in range(len(self.colStat)):
            if(self.colStat[i] < 640000):
                l.append(i)
        self.selectedfeatures=l
        print('\n Selected features   : {0}').format(self.selectedfeatures)
        print('\n Count of selected features : {0}').format(len(self.selectedfeatures))

    def generateNewfeature(self,fileName,writeFile):
        """
        Desc : Generate new Features.

        """
        print('\n Load Feature data : ')
        fp=csv.reader(open(fileName,'rb'))
        #writeFile='/nobackup/anikgaik/search/features/.csv'
        firstRow=True
        data=[]
        rowCount=0
        for row in fp:
            if(firstRow):
                #header=filter(lambda x:row.index(x) in self.selectedfeatures,row)
                header=[row[i] for i in self.selectedfeatures]
                #print('\n Length of header : {0}').format(len(header))
                #print('\n length of selected features : {0}').format(len(self.selectedfeatures))
                #print('header : {0}').format(header)
                data.append(header)
                firstRow=False

            else:
                rowCount+=1
                #dataRow=filter(lambda x:row.index(x) in self.selectedfeatures,row)
                dataRow=[row[i] for i in self.selectedfeatures]
                if(rowCount>=10000):
                    self.writeFile(data,writeFile)
                    data=[]
                    rowCount=0

                else:
                    data.append(dataRow)

        #print('\n Data : {0}').format(data)
        #self.getStat(data)

    def printAll(self):
        print('\n Column statistics   : {0}').format(self.colStat)



    def writeFile(self,data,fileName):
        #print('\n Writting File {0} : ').format(fileName)
        #fileName=self.dirName+"/"+fileName
        with open(fileName, 'ab') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(data)




