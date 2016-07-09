import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Visualization:
    def __init__(self):
        self.X=None
        self.Y=None

    def visualization_2d(self,dataset):
        colors = ['b', 'g', 'y', 'k', 'r']
        numinputs=dataset.shape[1]-1
        self.X=dataset[:,0:numinputs]
        self.Y=dataset[:,numinputs]
        Y=self.Y
        X=self.X
        #plt.scatter(X[:,0],Y,cmap=plt.cm.Paired)

        selectList=[]
        for i in range(len(Y)):
            if int(Y[i])==1:
                selectList.append(i)
        print('\n Selected Indices : {0}').format(selectList)
        Y=Y[selectList]
        X=X[selectList,:]
        lo = plt.scatter(X[:,0],X[:,2],c=Y, marker='o', color=colors[0])

        Y=self.Y
        X=self.X
        selectList=[]
        for i in range(len(Y)):
            if int(Y[i])==2:
                selectList.append(i)
        print('\n Selected Indices : {0}').format(selectList)

        Y=Y[selectList]
        X=X[selectList,:]
        ll = plt.scatter(X[:,0], X[:,2],c=Y, marker='s', color=colors[1])
        '''
        Y=self.Y
        X=self.X
        selectList=[]
        for i in range(len(Y)):
            if int(Y[i])==3:
                selectList.append(i)
        print('\n Selected Indices : {0}').format(selectList)
        Y=Y[selectList]
        X=X[selectList,:]
        l  = plt.scatter(X[:,0], X[:,2],c=Y, marker='*', color=colors[2])

        Y=self.Y
        X=self.X
        selectList=[]
        for i in range(len(Y)):
            if int(Y[i])==4:
                selectList.append(i)
        print('\n Selected Indices : {0}').format(selectList)
        Y=Y[selectList]
        X=X[selectList,:]
        a  = plt.scatter(X[:,0], X[:,2],c=Y, marker='x', color=colors[3])

        Y=self.Y
        X=self.X
        selectList=[]
        for i in range(len(Y)):
            if int(Y[i])==5:
                selectList.append(i)
        print('\n Selected Indices : {0}').format(selectList)
        Y=Y[selectList]
        X=X[selectList,:]
        h  = plt.scatter(X[:,0], X[:,2],c=Y, marker='D', color=colors[4])
        '''
        plt.legend((lo, ll),
           ('1', '2', '3', '4', '5'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)
        plt.xlabel('PCA_1')
        plt.ylabel('PCA_3')
        #plt.scatter(X[:,0],Y,cmap=plt.cm.Paired)
        plt.show()

    def visualization_3d(self,dataset):
        numinputs=dataset.shape[1]-1
        self.X=dataset[:,0:numinputs]
        self.Y=dataset[:,numinputs]
        Y=self.Y
        X=self.X
        selectList=[]
        for i in range(len(Y)):
            if int(Y[i])==5:
                selectList.append(i)
        print('\n Selected Indices : {0}').format(selectList)

        Y=Y[selectList]
        print(Y)
        X=X[selectList,:]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x=X[:,0]
        y=X[:,1]
        z=X[:,2]
        print('\n x : {0} , y : {1} , z : {2}').format(x,y,z)
        ax.scatter(x,y,z,c=Y,marker='o')
        plt.xlabel('1st feature')
        plt.ylabel('2nd feature')
        plt.show()

