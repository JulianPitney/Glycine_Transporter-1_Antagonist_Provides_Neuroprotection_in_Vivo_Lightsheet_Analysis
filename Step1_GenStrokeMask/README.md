# Lightsheet Deep Learning Analyse
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
* ![Graphic User Interface](https://github.com/JulianPitney/Glycine_Transporter1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/blob/7ffbd182da3bd279fea07e0823377d932f5c9425/Step1_GenStrokeMask/Capture.JPG ''Graphic User Interface'')
