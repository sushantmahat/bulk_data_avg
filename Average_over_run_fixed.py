# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:11:09 2021

@author: Mahat
"""

import numpy as np
import pandas as pd

#The labview code doesn't always "hit" the time delay points consistently.
#e.g. when asked to take 200 data between delay 0 to 100, it will take data at
# [0, 0.5, 1, ...] or sometimes [0.01, 0.51, ...]. usually I take one data per
#ps so this is not a bog deal. Sometimes, I do take data per half ps, so I 
#define a function that can round up to 0.5 ps units:

def my_round(x, base=.5):
  return round(base * round(float(x)/base),1)  



def myround(x, base=.5):
  return round(base * round(float(x)/base),1) 
#hardcoded for corrupt data; ignore. use average_now going forward
def average_old(file_name):
    raw_file  = file_name
    col_names = ['stg_pos','time delay','V_in','V_out','ratio','DVD'] 
    
    data_pd = pd.read_csv('raw/' + raw_file, sep='\t', names=col_names)
    
    #get the last 20 data points () we got repeats due to wrong data taking; fixed for later sets
    
    
    data_non_re = data_pd.iloc[-4020:] 
    
    data_non_re['time delay'] = data_non_re['time delay'].round(decimals = 0)
    
    data_averaged = data_non_re.groupby('time delay').mean()
    
    #print(data_averaged)
    
    data_averaged.to_csv('averaged' + raw_file)
    
    #data_non_re.to_csv('raw_file'+'averaged', index = False)
    #print(data_pd.head())
    #print(data_sorted.nunique())

#main function:    
def average_now(file_name, return_prefix = 'averaged_'):
    raw_file  = file_name
    col_names = ['stg_pos','time delay','V_in','V_out','ratio','DVD'] 
    
    data_non_re  = pd.read_csv( 'raw/' + raw_file,sep='\t', names=col_names)
    
    #get the last 20 data points () we got repeats due to wrong data taking; fixed for later sets
    
    
       
    data_non_re['time delay'] = data_non_re['time delay'].apply(myround)
    
    data_averaged = data_non_re.groupby('time delay').mean()
    
    #print(data_averaged)
    
    data_averaged.to_csv('averaged/' + return_prefix + raw_file)
    
    #data_non_re.to_csv('raw_file'+'averaged', index = False)
    #print(data_pd.head())
    #print(data_sorted.nunique())



'''
print(myround(5.1))   
col_names = ['stg_pos','time delay','V_in','V_out','ratio','DVD'] 
    
data_non_re  = pd.read_csv('Acoustic01_Si_2min_Ni_dep',sep='\t', names=col_names)    

data_non_re['time delay'] = data_non_re['time delay'].apply(myround)
print(data_non_re.head())
'''
#print(data_non_re.groupby('time delay').mean().head(n = 15))

