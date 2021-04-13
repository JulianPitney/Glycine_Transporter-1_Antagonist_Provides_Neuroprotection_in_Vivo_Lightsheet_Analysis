# Step 1: Gen Stroke Mask

This step is where a DCNN is used to segment the stroke region and background in each slice of the stitched scan. A binary mask is generated to represent the stroke region in each slice.

# Table of Contents
* [Purpose](#purpose)
* [Usage](#usage)
* [Troubleshooting](#troulbeshooting)
* [Contact](#contact)

# Purpose

# Usage

## 1. Install and Requirements
* `cd Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/Step1_GenStrokeMask/requirements`
* `conda create --name <myenv> --file spec-file.txt` Replace tokens marked as <token> with your own values.
* **Optional:** If Nvidia GPU is accessible  `conda install tensorflow-gpu`

## 2. Import trained weights
* 1. [click here to download](https://drive.google.com/drive/folders/1vak_PFfdLiy1uARrOCWuWO95iVOY5TNX?usp=sharing)
* 2. Copy the entire `weights` folder into `Step1_GenStrokeMask` folder.
* The desired file architecture should be:
> Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/Step1_GenStrokeMask/  
>> weights/  
>>> checkpoint  
>>> model.tf.data-00000-of-00002  
>>> model.tf.data-00001-of-00002  
>>> model.tf.index  

## 3. Predict
* `conda activate <myenv>`
* `cd  Step1_GenStrokeMask/src`
* `python predict.py`

# Troubleshooting

# Contact
* [Junzheng Wu](alchemistWu0521@gmail.com)
