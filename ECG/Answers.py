#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:10:25 2023

@author: schama
"""

from pyecg import ECGRecord
import os

# Question 1

def record_reader(path):
    files = sorted([x for x in os.listdir(path) if x.find(".hea") != -1])
    objectlist = []
    for i in range(len(files)):
        objectlist.insert(i, ECGRecord.from_wfdb(os.path.join(path,files[i]))) 
    output = {'record_files': files,
              'record_objs':objectlist}
    return output

# Question 2
# 

def heart_beats_summary(record):
    labels = [str(x) for x in record.annotations._labels]
    firsts = []
    for i in range(len(labels)):
        firsts.append(labels[i][0])
    beats = len(firsts) - firsts.count('+')
    time = record.duration*0.0166667
    mean_heart_rate = round(beats/time)
    normal = round(firsts.count('N')/beats, 2)
    output = {'heart_beats': beats,
              'mean_heart_rate': mean_heart_rate,
              'perc_normal_beats': normal
              }
    return output
          

#output = {'heart_beats': 303,
#          'mean_heart_rate': 80,
#          'perc_normal_beats': .70
#          }
          
