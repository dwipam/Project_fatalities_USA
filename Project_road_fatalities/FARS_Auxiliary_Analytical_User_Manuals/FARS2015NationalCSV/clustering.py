import pandas as pd
import numpy as np
from kmodes import kmodes




def kmodes(data):
    pass

def analysis_kmodes(data):
    pass

def kmeans(data):
    #1. Convert categorical data to one-hot encoding
    #2. remove durnken_dr variable from clustering
    #3. Output data with labeled clusters
    pass

def analysis_kmeans(data):
    #1. Compute Sum of Squared distance
    #2. plot how increase in K changes in Mean sum of sqaures
    #3. Plot how runing multiple interations for best K returns changes in cluster
    #Return best clustered data.
    pass

def read_data():
    data = pd.read_csv('filtered_fatalities.csv',sep="\t")
    return data

def main():
    data = read_data()
    kmeans_result = analysis_kmeans(data)
    kmodes_result = analysis_kmodes(data)


if __name__=='__main__':main()
