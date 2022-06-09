# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:31:47 2021

@author: smahat2
"""

import ExpDec_Res_Sine_fxn as sig_fit
#fits ration instead of V_in

import Average_over_run_fixed as avg
import glob
import numpy as np
import os

file_prefix   = 'Acoustic'
return_prefix = 'averaged_'

#import and average data:
true_str      = 'raw/' + file_prefix + '*'
file_paths     = glob.glob(true_str)
file_names    = [os.path.basename(x) for x in file_paths ]

for n, i in enumerate(file_names):
    avg.average_now(i, return_prefix)

#do the analysis:

fit_results = []
    
for n, i in enumerate(file_names):
    fit_results.append(sig_fit.fit_fxn(return_prefix + i, 5))
    

#output summary file ( tab delimited)

output_smr = open('Averaged_Summary_new_' + file_prefix, 'w')

for n, i in enumerate(fit_results):
    output_smr.write(file_names[n] + '\t ' )
    for j in i:
        output_smr.write(str(j) + '\t')
    output_smr.write("\n")
    
output_smr.close()