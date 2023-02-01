#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:10:25 2023

@author: schama
"""

print(2+2)
import sys
print(sys.executable)

import numpy as np
from pyecg import ECGRecord
import os
path = "/Users/schama/Desktop/Mirror/00FSU/00CoursesSpring2023/DataHealth/Week3/HW3/ecg-data-analysis-RSchama/test_folder/Data/"
files = sorted([x for x in os.listdir(path) if x.find(".hea") != -1])
print(files)

record = ECGRecord.from_wfdb("/Users/schama/Desktop/Mirror/00FSU/00CoursesSpring2023/DataHealth/Week3/HW3/ecg-data-analysis-RSchama/test_folder/Data/208.hea")
record.shape

ECGRecord(name, time)

print(record)
record.__dict__
record.duration
record.lead_names
len(record.signals)
a = record.signals
# a is a list with two sublists, the 0 element has 650000 negative numbers and the [1] has the same size with positive numbers below zero
record.n_sig
record.p_signal.shape
#aboe seems to be similar to a but in an array style! easier tod eal?, looking at it it seems positive and negaive are in both lists?
b = record.p_signal

record
vars(record)
type(objectlist[1])
vars(objectlist[1])

print(record.annotations._labels)
record.signals




########
for i in range(len(files)):
    objectlist.append(str(ECGRecord)+str(i))

objectlist = []
for i in range(len(files)):
    objectlist.insert(i, ECGRecord.from_wfdb(os.path.join(path,files[i]))) 
    
filedate = {file: ECGRecord.from_wfdb(os.path.join(path,file)) for file in files }
####################

# Question 1
def record_reader(path):
    files = sorted([x for x in os.listdir(path) if x.find(".hea") != -1])
    objectlist = []
    for i in range(len(files)):
        objectlist.insert(i, ECGRecord.from_wfdb(os.path.join(path,files[i]))) 
    output = {'record_files': files,
              'record_objs':objectlist}
    return output

re = record_reader(path)
re[record_objs]          

for i in re:
    print(i, re[i])  
for key, value in test_dict.items():
    print(key, value)        
          
####################
# Question 2
import pandas as pd

print(record.annotations._labels)
c = record.annotations._labels
print(c[100])
l = str(c[0])
newArray = [str(x) for x in record.annotations._labels]
newArray[0][0]
firsts = []
for i in range(len(newArray)):
    firsts.append(newArray[i][0])
x = pd.Series(firsts)
# counting number of unique objects in a list
set(firsts)
len(set(firsts))
# counting a specific entry
firsts.count('+')

time = record.duration*0.0166667

beats = len(firsts) - firsts.count('+') - firsts.count('~') - firsts.count('|')

# below is still missing double wuatoes "
nonbeats = ["+","~","|","[","]","!","x","(",")","p","t","u","`","'","^","s","T","*","D","=","@"]
discount = 0 
for i in nonbeats:
    discount += firsts.count(i)
beats2 = len(firsts) - discount
    
mean_heart_ratex = beats/time
normal = int(firsts.count('N')/beats2 * 100)
normal2 = round(firsts.count('N')/beats2, 2)
record??
record.annotations


def heart_beats_summary(record):
    labels = [str(x) for x in record.annotations._labels]
    firsts = []
    for i in range(len(labels)):
        firsts.append(labels[i][0])
    #nonbeats = ["+","~","|","[","]","!","x","(",")","p","t","u","`","'","^","s","T","*","D","=","@"]
    #discount = 0 
    #for i in nonbeats:
    #    discount += firsts.count(i)
    #beats = len(firsts) - discount
    beats = len(firsts) - firsts.count('+')
    time = record.duration*0.0166667
    mean_heart_rate = round(beats/time)
    normal = round(firsts.count('N')/beats, 2)
    output = {'heart_beats': beats,
              'mean_heart_rate': mean_heart_rate,
              'perc_normal_beats': normal
              }
    return output

record2 = ECGRecord.from_wfdb("/Users/schama/Desktop/Mirror/00FSU/00CoursesSpring2023/DataHealth/Week3/HW3/ecg-data-analysis-RSchama/test_folder/Data/212.hea")
heart_beats_summary(record2)

time2 = record2.time    
record2.info    
# 1 millisecond is equal to 1,6667e-5 minutes
# heart beat is beats per minute (BPM)

assert output['heart_beats'] == pytest.approx(2762, 2)
          assert output['mean_heart_rate'] == pytest.approx(91, 1)
  >       assert output['perc_normal_beats'] == pytest.approx(.33, .05)
          
