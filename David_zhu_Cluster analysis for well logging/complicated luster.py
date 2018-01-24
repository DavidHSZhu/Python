__author__ = 'Administrator'
import os
import pandas as pd #import panda
from sklearn.cluster import AgglomerativeClustering#import Clustering 
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
ex14 = pd.read_csv('ying8_1.txt',header = 0,sep='\s+')#import well logging data from file of ying8.txt

print(ex14.iloc[:,1:20])   #get the first column of data
kmeans = KMeans(n_clusters=3)# group all of data into 3 sections,standard by 0,1,2
kmeans.fit(ex14)

kmeans_pred = kmeans.fit_predict(ex14.iloc[:,1:20])
print ('kmeans cluster:',kmeans_pred)
ex14[u'类型']=kmeans_pred
print( ex14)