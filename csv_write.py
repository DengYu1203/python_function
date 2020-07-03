"""
save the output_list as csv file.
"""

import os
import csv

# set the output dir path
code_path = os.path.dirname(os.path.realpath(__file__))

output_dir = os.path.join(code_path,'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_data_dir = os.path.join(output_dir,'csv')
if not os.path.exists(csv_data_dir):
    os.makedirs(csv_data_dir)

def csv_write(output_list):
    csv_path = os.path.join(csv_data_dir,'output.csv')
    with open(csv_path,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id','label']) # the first row of the csv file
        for data in output_list:
            row = []
            row.append(int(data[0]))
            row.append(int(data[1]))
            writer.writerow(row)
    return