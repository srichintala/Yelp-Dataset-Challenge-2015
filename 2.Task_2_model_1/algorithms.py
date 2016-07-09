from sklearn.naive_bayes import MultinomialNB
from sklearn  import linear_model
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import svm
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import BernoulliRBM

"""
Name :  Aniket Gaikwad
description : This file implements all the classifiers used.
"""

class NaiveBayes:
    """
        Naive Bayes Implementation
    """

    def __init__(self):
        self.model=None
        self.prediction=None

    def learn(self,Xtrain,Ytrain):
        model=MultinomialNB(fit_prior=True)
        model.fit(Xtrain,Ytrain)
        self.model=model

    def predict(self,Xtest):
        model=self.model
        self.prediction=model.predict(Xtest)
        return self.prediction


class LogisticRegression:
    """
    L2-Regularized Logistic regression Implementation
    """
    def __init__(self):
        self.model=None
        self.prediction=None

    def learn(self,Xtrain,Ytrain):
        model=linear_model.LogisticRegression(penalty='l2',C=1.0,tol=0.0001,multi_class='multinomial',solver='newton-cg')
        model.fit(Xtrain,Ytrain)
        self.model=model

    def predict(self,Xtest):
        model=self.model
        self.prediction=model.predict(Xtest)
        return self.prediction


class GradientBoost:
    """
    Gradient Boost Algorithm Implementation
    """
    def __init__(self):
        self.model=None
        self.prediction=None

    def learn(self,Xtrain,Ytrain):
        model=GradientBoostingRegressor(learning_rate =0.1)
        model.fit(Xtrain,Ytrain)
        self.model=model

    def predict(self,Xtest):
        model=self.model
        self.prediction=model.predict(Xtest)
        return self.prediction

class DeepBeliefNetwork:
    """
    Deep Belief Network Implementation
    """
    def __init__(self,hiddenLayers,learning_rate):
        self.model=None
        self.data=None
        self.hiddenLayers=hiddenLayers
        self.learning_rate=learning_rate

    def learn(self,Xtrain,Ytrain):
        model = BernoulliRBM(n_components=self.hiddenLayers,learning_rate=self.learning_rate)
        self.model=model.fit(Xtrain,Ytrain)
        return self.model

    def transform(self,data):
        model=self.model
        self.data=model.transform(data)
        return self.data

class SVM:
    """
    SVM with linear kernel Implementation
    """
    def __init__(self):
        self.model=None
        self.prediction=None
        #self.kernelType=kernelType

    def learn(self,Xtrain,Ytrain):
        #model=svm.SVR(kernel='sigmoid',gamma='auto',C=50)
        #print('\n Kernel : {0}').format(self.kernelType)
        model=svm.SVR(kernel='linear',gamma='auto',C=100)
        model.fit(Xtrain,Ytrain)
        self.model=model

    def predict(self,Xtest):
        model=self.model
        self.prediction=model.predict(Xtest)
        return self.prediction


class DecisionTreeReg:
    """
    Decision Tree Regression Implementation
    """
    def __init__(self):
        self.model=None
        self.prediction=None

    def learn(self,Xtrain,Ytrain):
        model=DecisionTreeRegressor(max_depth=5)
        model.fit(Xtrain,Ytrain)
        self.model=model

    def predict(self,Xtest):
        model=self.model
        self.prediction=model.predict(Xtest)
        return self.prediction

class DecisionTreeClassifier:
    """
    Decision tree classifier Implementation
    """
    def __init__(self):
        self.model=None
        self.prediction=None

    def learn(self,Xtrain,Ytrain):
        model=DecisionTreeClassifier()
        model.fit(Xtrain,Ytrain)
        self.model=model

    def predict(self,Xtest):
        model=self.model
        self.prediction=model.predict(Xtest)
        return self.prediction

class RandForest:
    """
    Random forest with 100 trees Implementation
    """
    def __init__(self):
        self.model=None
        self.prediction=None

    def learn(self,Xtrain,Ytrain):
        model=RandomForestRegressor(n_estimators=100)
        model.fit(Xtrain,Ytrain)
        self.model=model

    def predict(self,Xtest):
        model=self.model
        self.prediction=model.predict(Xtest)
        return self.prediction




