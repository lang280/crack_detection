# Crack Detection and Segmentation
## Introduction
Based on [khanhha/crack_segmentation](https://github.com/khanhha/crack_segmentation)  
Updated to fit newer version of python and cuda  
Remove and replace the deprecated code  
Some improvements on usabilities  

## System Requirements
Ubuntu (Recommand 22.04 LTS)  
Cuda (Recommand 11.6)  
Anaconda  

## Environment Preparation
### Create and Enter Conda environment
```
conda create --name crack python=3.10
conda activate crack
```
### Dependencies Installation
```
conda install matplotlib scipy numpy tqdm pillow
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
conda install -c conda-forge opencv
```
[Other Versions of Pytorch](https://pytorch.org/get-started/locally/)  

## Pre-Trained Model
Use the pre-trained model in order to run the crack detection algorithm without training  
Download [model_unet_vgg_16_best.pt](https://drive.google.com/file/d/1wA2eAsyFZArG3Zc9OaKvnBuxSAPyDl08/view) and put it in ./Models

