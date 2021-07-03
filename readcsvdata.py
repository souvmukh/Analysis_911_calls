# -*- coding: utf-8 -*-
"""
Loading data from CSV into Pandas Data frame.

"""
import pandas as pd


class ReadData(object):

    def __init__(self,filename = '911.csv'):

        self.dframe = pd.read_csv(filename)
        self.dframe.drop(labels='e', axis = 1, inplace = True) 
        #loads a dataframe & removes the irrelevant data in column headed e

    def getmetadata(self):
        return self.dframe.info
        #Information about the loaded data-frame

    def gethead(self):
        
        return self.dframe.head()
        # top 5 sample data in the data-frame

    def set_rnd_data(self):
        
        return self.dframe.sample(frac = 1)
        #randomised output of the full data-frame

    def get_trng_set(self, count):
        
        return self.dframe.sample(frac = 0.7)
        #randomised output of the 70% of the data-frame

    def get_test_set(self, count):
        
        return self.dframe.sample(frac = 0.3)
        #randomised output of the 30% of the data-frame

    def __str__(self):
        
        return "Data Manipulation Class using Pandas"


if __name__ == '__main__':
    t = ReadData('F:/Python Projects/Data/911.csv')
    print(t.gethead())
