# Step 2: Gen Stroke Mask

This step is where a DCNN is used to segment the stroke region and background in each slice of the stitched scan. A binary mask is generated to represent the stroke region in each slice.

# Table of Contents
* [Purpose](#purpose)
* [Usage](#usage)
* [Troubleshooting](#troulbeshooting)
* [Contact](#contact)

# Purpose
This step has 2 purposes. The first is to automatically estimate the total stroke volume in each scan. The second is to provide an overlay of the stroke region during the cropping step. This overlay helps guide researchers when choosing an ROI to crop.

# Usage

**Software Requirements:**

| Name | Version |
| ----------- | ----------- |
| Windows | 10 |
| Anaconda | 2020.11 |
| Python | 3.6.7 |
| tensorflow-gpu (optional) | 2.4.1 |

**Inputs:** FILL OUT LATER FRANK

**Outputs:** FILL OUT LATER FRANK

**Steps:**

1. First we need to set up our environment and install dependencies. To do this, run the following commands in order.   

- `cd Glycine_Transporter-1_Antagonist_Provides_Neuroprotection_in_Vivo_Lightsheet_Analysis/Step2_GenStrokeMask/requirements`

- `conda create --name stroke_detector_env --file spec-file.txt`

- **Optional:** If Nvidia GPU is accessible then run  `conda install tensorflow-gpu`


2. Next we need to import the trained weights for our stroke detection network. First, [click here to download](https://drive.google.com/drive/folders/1vak_PFfdLiy1uARrOCWuWO95iVOY5TNX?usp=sharing) the weights. Once downloaded, copy the entire `weights` folder into the `Step2_GenStrokeMask`
folder. The correct file structure is:
> Glycine_Transporter-1_Antagonist_Provides_Neuroprotection_in_Vivo_Lightsheet_Analysis/Step2_GenStrokeMask/  
>> weights/  
>>> checkpoint  
>>> model.tf.data-00000-of-00002  
>>> model.tf.data-00001-of-00002  
>>> model.tf.index  

3. Now that our environment, dependencies and weights are set up, we can run the detector. To do this, run the following commands in order.

- `conda activate stroke_detector_env`

- `cd  Step2_GenStrokeMask/src`

- `python predict.py`

# Troubleshooting

No common problems reported yet.

# Contact
* [Junzheng Wu](alchemistWu0521@gmail.com)
