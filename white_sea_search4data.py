# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:02:58 2021

@author: F1
"""

import os
import shutil

import pandas as pd


meta_file_path = (r'd:/SCIENCE/2020/badulin_rfbr/crossovers_J2J3_self/'
                   'white_sea_apr2021/white_sea_meta.xlsx')


meta = (pd.read_excel(meta_file_path))
#print(meta)

mission = 1
if mission != 1:
    mission_path = r's:/Shared with me/jason-{}/sgdr_d'.format(mission)
else:
    mission_path = r's:/Shared with me/jason-{}/sgdr_e'.format(mission)

cycles = list(sorted(os.listdir(mission_path)))

stype = int('{0:}{0:}'.format(mission))
if stype == 11:
    stype = 22

s1 = meta.query('stype == @stype')['orbit_1'].values
s2 = meta.query('stype == @stype')['orbit_2'].values

f_copy = True   #False

big_box = []
full_files = []
fdict = {}

dst_folder = r'e:/ALT/white_sea_selfcross_db/jason_{}/'.format(mission)
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)
    
t = 0
for f_cycle in cycles:
    
    in_cycle = '{}/{}'.format(mission_path, f_cycle)
    zip_files = sorted(os.listdir(in_cycle))
    
#    val_files = [ffile for ffile in zip_files if int(ffile.split('_')[3]) in s1
#                 or int(ffile.split('_')[3]) in s2]

    f_files = ['{}/{}'.format(in_cycle, ffile) for ffile in zip_files if int(ffile.split('_')[3]) in s1
                 or int(ffile.split('_')[3]) in s2]

    if f_copy:
        for src in f_files:
            
            
            #src = '{}/{}'.format(in_cycle, src_file)
            src_file = src.split('/')[-1]
            dst = '{}/{}'.format(dst_folder, src_file)
            if os.path.exists(dst): # and os.path.getsize(src) == os.path.getsize(dst):
#                continue
                if os.path.getsize(src) != os.path.getsize(dst):
                    print('ReWrite {} - - -> {}'.format(src, dst))
                    shutil.copy(src, dst)
                    t += 1                    
            else:
                print('Download ', t, src_file)
                
                shutil.copy(src, dst)
                t += 1
            
        
#    fdict[f_cycle] = val_files
#    big_box.extend(val_files)
    full_files.extend(f_files)

    
full_files = list(sorted(full_files))
print('Len {}'.format(len(full_files)))
