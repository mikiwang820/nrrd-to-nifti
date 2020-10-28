#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:13:32 2020

@author: wangmeiqi
"""


import os
import nrrd
import nibabel as nib
import numpy as np
import SimpleITK as sitk 

save_route = '/Users/wangmeiqi/code_and_data/HCC/ntuh/hcc_ntuh_niigz_1012'
main_route = '/Users/wangmeiqi/code_and_data/HCC/ntuh/HCC_labeled'
filename = 'temp'
route = os.path.join(main_route, filename)
train = 'train'
val = 'val'
train_names = []
train_label_names = []
val_names = []
val_label_names = []
data = {}
data['validation'] = []
dir_ = []
path = []





for root, dirs, files in os.walk(route):
    #print(root)
    for file in files:
        #print(file)
        if file != '.DS_Store':
            filename = os.path.join(root, file)
            read_img = sitk.ReadImage(filename)
            name = root.split("/")
            output_path = os.path.join(save_route, file[:-5] + '_' + name[-1] + '.nii.gz')
            sitk.WriteImage(read_img,  output_path)
            print("fininshing: " + output_path)



