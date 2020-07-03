"""
Load/save the pytorch training model file.
"""

import os
import torch
from Net import Net # Net model

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# set the output dir path
code_path = os.path.dirname(os.path.realpath(__file__))

output_dir = os.path.join(code_path,'..','output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

model_dir = os.path.join(output_dir,'model')
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

def save_model(model):
    segnet_save_path = os.path.join(model_dir,'model.pth')  # model path to save
    torch.save(model.state_dict(),segnet_save_path)
    return

def load_model():
    segnet_save_path = os.path.join(model_dir,'model.pth')  # model path to load
    model = Net().to(device)   # replace the Net model to your own Net
    model.load_state_dict(torch.load(segnet_save_path))
    return model