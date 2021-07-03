# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:10:48 2021

@author: Souvik
"""

from matplotlib import pyplot as plt
import seaborn as sns
from readcsvdata import ReadData
import pandas as pd

class ShowData(ReadData):
    
   
    def getreason_plt(self):
        
        #add a column for reasons of 911 call by striping title using lambda function
        #which has information like EMS, Fire, Traffic
        
        self.dframe['reason'] = self.dframe['title'].apply(lambda t : t.split(':')[0])
        sns.countplot(x = 'reason', data= self.dframe)
        
    
    def getdatetime(self):
        self.dframe['timeStamp'] = pd.to_datetime(self.dframe['timeStamp'])
        
        self.dframe['year'] = self.dframe['timeStamp'].apply(lambda time : time.year)
        
        self.dframe['month'] = self.dframe['timeStamp'].apply(lambda time : time.month)
        
        self.dframe['hour'] = self.dframe['timeStamp'].apply(lambda time : time.hour)
        
        self.dframe['day']= self.dframe['timeStamp'].apply(lambda time : time.dayofweek)
        #returns the day of the week as int - Mon:0, Tue:1,...,Sun:6
        
        return self.dframe
    
    
    def getyearly_plt(self,df):
        self.df = df
        self.df['reason'] = self.df['title'].apply(lambda t : t.split(':')[0])
        
        fig, ax = plt.subplots(1,2)# Allows 2 sidebyside plot via pyplot
        
        sns.countplot(x = 'year', data= self.df, ax = ax[0])
        sns.countplot(x = 'year', hue = 'reason', data = self.df, ax = ax[1])
        
        #fig.show() #Displays but doesnt save the plot
        fig.savefig('YearlyPlot.png')

    
    def getmonthly_plt(self,df):
        self.df = df
        self.df['reason'] = self.df['title'].apply(lambda t : t.split(':')[0])
        
        fig, ax = plt.subplots(1,2)# Allows 2 sidebyside plot via pyplot
        
        sns.countplot(x = 'month', data= self.df, ax = ax[0])
        sns.countplot(x = 'month', hue = 'reason', data = self.df, ax =ax[1])
        
        fig.savefig('MontlyPlot.png')
    
    
    def gethourly_plt(self,df):
        self.df = df
        self.df['reason'] = self.df['title'].apply(lambda t : t.split(':')[0])
        
        fig, ax = plt.subplots(1,2)# Allows 2 sidebyside plot via pyplot
        
        sns.countplot(x = 'hour', data=self.df, ax = ax[0])
        sns.countplot(x = 'hour', hue = 'reason', data = self.df, ax = ax[1])
        
        fig.savefig('HourlyPlot.png')
        
    
    def getdaily_plt(self,df):
        self.df = df
        self.df['reason'] = self.df['title'].apply(lambda t : t.split(':')[0])
        
        fig, ax = plt.subplots(1,2)
        
        dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
        #Mapping each number to a day in week
        self.df['day'] = self.df['day'].apply(lambda d : dmap[d])
        
        sns.countplot(x = 'day', data=self.df, ax = ax[0])
        sns.countplot(x = 'day', hue = 'reason', data = self.df, ax = ax[1])
        
        fig.savefig('DailylyPlot.png')
        
    def getpltbyzip(self):
        sns.countplot(x='zip', data=self.dframe, palette='muted')
    
        
if __name__ == "__main__":
    display = ShowData('F:/Python Projects/Data/911.csv')
    display.getreason_plt()
    df = display.getdatetime()
    display.getyearly_plt(df)
    display.getmonthly_plt(df)
    display.gethourly_plt(df)
    display.getdaily_plt(df)
    display.getpltbyzip()
    