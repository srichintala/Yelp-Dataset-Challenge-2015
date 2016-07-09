import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error, accuracy_score, roc_auc_score, jaccard_similarity_score, r2_score

from math import sqrt

test = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/FeatureOutput/OutputTest.csv')
pred = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/prediction.csv')

test.stars = np.array(test.stars)

test_rat = test.stars

pred.Prediction = np.array(pred.Prediction)

pred_rat = pred.Prediction

#R2 score

R2 = r2_score(test_rat, pred_rat)

print R2

#Weighted R2

WeightR2 = r2_score(test_rat, pred_rat,multioutput='variance_weighted')

print WeightR2


##jaccard_similarity_score

JSS = jaccard_similarity_score(test_rat, pred_rat)
#
JSS_N = jaccard_similarity_score(test_rat, pred_rat,normalize=False)
#
print JSS 
print JSS_N

#AUC score

AUC_roc = roc_auc_score(test_rat, pred_rat)

print AUC_roc

#MSE = mean_squared_error(test.stars, pred.Prediction)
#
#MSE = (test.stars - pred.Prediction)**2  
k = (test_rat - pred_rat)

#number of items perfectly matching
m0 = k [k==0].shape[0]

m1 = k[abs(k)==1].shape[0]

m2 = k[abs(k)==2].shape[0]

k[abs(k)<=2].shape[0]

correct = 0
for i in range(len(pred_rat)):
    if test_rat[i] - pred_rat[i] == 0:
       correct += 1
    elif abs(test_rat[i] - pred_rat[i]) == 1:
        correct += 1
    #elif abs(test_rat[i] - pred_rat[i]) == 2:
    #    correct += 0.60
print (correct/float(len(test_rat))) * 100.0



#MSE = 


#less than or equal to two = 250767

#equal to zero 122394

#equal to one 90119L

#equal to two 38254




#shape(k[k<=1&k!=0 ]) 

#MSE = sum(k)/float(k.shape[0])

#print MSE

#RMSE = np.sqrt(MSE)

#print RMSE

#score = accuracy_score(test_rat, pred_rat)

#print score

