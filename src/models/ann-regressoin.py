# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:38:46 2017

@author: user
"""
import numpy as np
import pandas as pd
#import keras
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


#Importing dataSet
trainset = pd.read_csv('train.csv')
testset = pd.read_csv('test.csv')
temp = trainset.SalePrice
trainset.drop('SalePrice',1,inplace=True)

dataset = trainset.append(testset)
dataset.reset_index(inplace=True)
dataset.drop('index',1,inplace=True)

#data preprocessing
dataset.MSSubClass.isnull().values.any()
dataset.MSZoning.isnull().values.any()

dataset['MSZoning'] = dataset['MSZoning'].map(lamba r: )
dataset.Neighborhood.isnull().values.any()

