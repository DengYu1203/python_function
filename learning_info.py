"""
Record the the list from the deep learning process.
You can also use this funcion to record some data(list) you want to save/load.
I use json file to save the small size list, but some large file should save as numpy file as recommand.
"""

import os
import json
import numpy as np

# set the output dir path
code_path = os.path.dirname(os.path.realpath(__file__))

output_dir = os.path.join(code_path,'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

info_data_dir = os.path.join(output_dir,'info')
if not os.path.exists(info_data_dir):
    os.makedirs(info_data_dir)

# the list you want to save/load
data_list = []  # small size list
img_list = []   # large size list(should be converted to np.array type)

def save_info():
    global data_list
    global img_list
    data_path = os.path.join(info_data_dir,'data.json')
    img_list_path = os.path.join(info_data_dir,'img')

    with open(data_path,'w') as file:
        json.dump(data_list,file)
    np.save(img_list_path,np.array(img_list))

    return

def load_info():
    data_path = os.path.join(info_data_dir,'data.json')
    img_list_path = os.path.join(info_data_dir,'img.npy')

    with open(data_path,'r') as file:
        load_data_list = json.load(file)
    load_img_list = np.load(img_list_path)

    return load_data_list, load_img_list