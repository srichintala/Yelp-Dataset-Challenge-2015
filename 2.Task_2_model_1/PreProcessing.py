import csv
import numpy as np
import pandas as pd
import csv
import math

"""
Name : Aniket Gaikwad
Desc : This file contains the pre-processing steps like feature selection, feature descritization,feature removal etc
"""

class preprocessing:
    def __init__(self):
        self.data=None

    def replaceNull(self,fileName,writeFile):
        """
        Desc : Replace the null or NA entries in file
        Args:
            fileName: Train file
            writeFile: Modified File

        Returns: None

        """
        print('\n Function call replaceNull starts : ')
        fp=csv.reader(open(fileName,"rb"))
        rowcount=0
        data=[]

        for row in fp:
            rowcount+=1
            if((rowcount%1000)==0):
               self.writeFile(data,writeFile)
               data=[]
            newRow=['NA' if entry=='' else entry for entry in row]
            data.append(newRow)
            print('newRow : {0}').format(newRow)

        self.writeFile(data,writeFile)

    def removeFeature(self,fileName,writeFile):
        '''
            Remove the Restaurant open and close time.
            Also replace null by 'NA'
        '''
        print('\n Function call removeFeature starts : ')
        fp=csv.reader(open(fileName,"rb"))
        rowcount=0
        data=[]

        for row in fp:
            rowcount+=1
            if((rowcount%1000)==0):
                Adata=self.filterCols(data)
                data=Adata.tolist()
                self.writeFile(data,writeFile)
                data=[]
            newRow=['NA' if entry=='' else entry for entry in row]
            data.append(newRow)
            #print('newRow : {0}').format(newRow)


        Adata=self.filterCols(data)
        data=Adata.tolist()
        self.writeFile(data,writeFile)


    def filterCols(self,data):
        """
        Desc : Filter columns between 9 to 23
        Args:
            data: datatset

        Returns: newdataset

        """
        filterCols=[]
        for x in range(24):
            if x >=9 and x <=23:
                filterCols.append(x)

        dataset=np.array(data)
        newDataset=np.delete(dataset,filterCols,1)
        print('\n NewDataset : {0}').format(newDataset)
        return newDataset

    def featureDiscretization(self,fileName,writeFile):
        """
        Desc : Descritize the features, Generate metadata for categories.

        """
        print('\n featureDiscretization starts ....')
        df=pd.read_csv(fileName,delimiter=',')
        df=df.fillna('NA')

        listOfcols=list(df.columns.values)
        d={}
        psudoD={}
        exclude=['user_id','business_id','day','month','year','votes_cool','votes_funny','votes_useful','label','stars','attributes_Price_Range','review_count',\
                 'chinese','fastfood','american(traditional)','mediterranean','japanese','french','vegetarian','sushibars','pizza','mexican','food','sportsbars',\
                 'asianfusion','bars','thai','breakfast&brunch','delis','seafood','restaurants','steakhouses','barbeque','buffets','pubs','burgers','italian','sandwiches',\
                 'american(new)','nightlife']

        for entry in listOfcols:
            if entry in exclude:
                continue
            uniqueList=pd.unique(df[entry])
            d[listOfcols.index(entry)]={}
            psudoD[entry]={}
            addMe=1
            for x in uniqueList:
                d[listOfcols.index(entry)][str(x)]=addMe
                psudoD[entry][str(x)]=addMe
                addMe+=1

        print('\n Writting Metadata ....')
        metadata=[]
        for key,val in psudoD.iteritems():
            temp=[]
            temp.append(key)
            for newKey,newVal in val.iteritems():
                temp.append(newKey)
                temp.append(newVal)
            metadata.append(temp)

        self.writeFile(metadata,'D:\\Fall 2015\\Search\\YELP Challenge\\Yelp-Dataset-Challenge-2015\\Task_2\\metadata.csv')


        fp=csv.reader(open(fileName,"rb"))
        rowcount=0
        data=[]
        header=True
        for row in fp:
            if header:
                header=False
                data.append(row)
                continue
            rowcount+=1
            if((rowcount%1000)==0):
                self.writeFile(data,writeFile)
                data=[]
            newRow=[]

            newRow=[d[row.index(entry)][entry] if d.has_key(row.index(entry)) else entry for entry in row]
            data.append(newRow)
            #print('newRow : {0}').format(newRow)
            #print('data : {0}').format(data)
        self.writeFile(data,writeFile)





    def writeFile(self,data,fileName):
        """
        Desc :  Write contents to file.

        """
        with open(fileName, 'ab') as fw:
            a = csv.writer(fw, delimiter=',')
            a.writerows(data)
