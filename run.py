#!/usr/bin/env python
import os
import shutil
import sys

# change to script dir
os.chdir("./Code")

# default input, output, model
modle_type = "vgg16"
modle_dir = "../Models/model_unet_vgg_16_best.pt"
input_dir = "../Data/Inputs"
output_dir = "../Data/Outputs"

''' update input, output, model from cmd line arguments '''
# update input output directories
if len(sys.argv) >= 2:
    input_dir = sys.argv[1]
if len(sys.argv) >= 3:
    output_dir = sys.argv[2]

# update model directory and model type
if len(sys.argv) >= 4:
    modle_dir = sys.argv[3]
if len(sys.argv) >= 5:
    modle_type = sys.argv[4]

''' clean previous output '''
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)


''' prepare arguments for command '''
#bash_cmd = "python ./inference_unet.py  -img_dir ../Data/Inputs -out_viz_dir ../Data/Outputs/OUT_VIZ_DIR -out_pred_dir ../Data/Outputs/OUT_PRED_DIR -model_path ../Models/model_unet_vgg_16_best.pt -model_type vgg16"
bash_cmd = "python ./inference_unet.py"
# modle info
bash_cmd += " -model_type " + modle_type + " -model_path " + modle_dir
# input directory
bash_cmd += " -img_dir " + input_dir
# output crack mask directory
bash_cmd += " -out_pred_dir " + output_dir + "/Crack_Masks"
# output visualizations directory
bash_cmd += " -out_viz_dir " + output_dir + "/Visualizations"

''' run model '''
os.system(bash_cmd)

# back to start dir
os.chdir("..")
