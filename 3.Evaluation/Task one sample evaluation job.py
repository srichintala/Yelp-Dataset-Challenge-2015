import pandas as pd
import numpy as np
groundtruth = pd.read_csv('E:Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/GT.csv')
output = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT10_lmj.csv')
output2 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT20_lmj.csv')
output3 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT30_lmj.csv')
output4 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT40_lmj.csv')
output5 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT50_lmj.csv')
output6 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT60_lmj.csv')
output7 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT70_lmj.csv')
output8 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT80_lmj.csv')
output9 = pd.read_csv('E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/New folder/OT90_lmj.csv')

groundtruth = np.array(groundtruth)
lis = []
gtlis = []
precision = []
recall = []
output = np.array(output)
tot_true_positives = 0
tot_false_positives = 0
tot_false_negatives = 0

for i in range(1,len(output[:,2])):
    #print i
    if pd.isnull(output[i,2]):
        otlis = []
    else :
        otlis = output[i,2].split(', ')
    #print output[i,1]
    if pd.isnull(groundtruth[i,2]):
    #if groundtruth[i,2][i,2].dtype == str and np.isnan(groundtruth[i,2]):
        gtlis = []
    else :
        gtlis = groundtruth[i,2].split(', ')
    true_positives = len(set(otlis) & set(gtlis))
    false_positives = len(set(otlis) - set(gtlis))
    false_negatives = len(set(gtlis) - set(otlis))

    if (float(true_positives)+float(false_positives)) :
        precision.append(float(true_positives) / (float(true_positives)+float(false_positives)))
    else :
        precision.append(0)
    
    if (float(true_positives)+float(false_negatives)) :
        recall.append(float(true_positives) / (float(true_positives)+float(false_negatives)))
    else :
        recall.append(0)
    
    tot_true_positives =+ true_positives
    tot_false_positives =+ false_positives
    tot_false_negatives =+ false_negatives
    #print true_positives
    #print false_positives


k = 0
data = []
pre = []
reca = []
for i in range(1,781):
    print i
    
     #precision[i] > .3 and recall[i] > 0.3:
        #k = k + 1
    #col.append(output[i,1])
     #   pre.append(precision[i])
     #   reca.append(recall[i])
    #data.append(col)

        
    print output[i,1], str(','),precision[i], str(',') ,recall[i]
#print k

precision = np.array(precision)
recall = np.array(recall)
f1 = float(2) * ((precision * recall) / (precision + recall))
print f1

pre = np.array(pre)
reca = np.array(reca)
print pre.mean()
print reca.mean()

