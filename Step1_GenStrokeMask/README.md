# Lightsheet Deep Learning Analyse
## 0. Introduction(What and Why)
This step is for segmenting the Stroke region in the scans using a convolutional deep learning structure `Bisenet`. The identified stroke region will be used for cropping the scans. Besides, the stroke volume is also calculated in this step.
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
![Graphic User Interface](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/blob/eb47c6f3e88870df8a20cc121771cba9c0b1b81a/Step1_GenStrokeMask/Capture.JPG)
### 1. Generate stroke mask
* Select the input folder and output folder.
* For only next step use: Tickle the `Stroke` only, with `Normal` and `Background` unchecked.
* Then, click the `Run` button for generating the stroke masks.
* The GUI will be out of response for a while, you may check the progress in the terminal.
### 2. Optional: Calculate the stroke volume
* After generating the masks, you might need to calculate the stroke volume. Keep all the settings as it is in the previous step and simply click on the button of `Calculate Volume`.
* You will find a pie chart generated in the output folder.

## Reference
Yu, C., Wang, J., Peng, C., Gao, C., Yu, G., & Sang, N. (2018). Bisenet: Bilateral segmentation network for real-time semantic segmentation. In Proceedings of the European conference on computer vision (ECCV) (pp. 325-341).
