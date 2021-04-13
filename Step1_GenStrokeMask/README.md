# Lightsheet Deep Learning Analyse
## 1. Install and Requirements
* `git clone https://github.com/alchemistwu/lightsheetDL.git`
* `cd lightsheetDL/requirements`
* `conda create --name <myenv> --file spec-file.txt` Replace tokens marked as <token> with your own values.
* **Optional:** If Nvidia GPU is accessible  `conda install tensorflow-gpu`
## 2. Download trained weights [click here to download](https://drive.google.com/drive/folders/1vak_PFfdLiy1uARrOCWuWO95iVOY5TNX?usp=sharing)
## 3. Copy the entire `weights` folder into the root directory of lightsheetDL project. 
* The desired file architecture should be:
* lightsheetDL\  
    └weights\  
        ├─weights\checkpoint  
        ├─weights\model.tf.data-00000-of-00002  
        ├─weights\model.tf.data-00001-of-00002  
        └weights\model.tf.index  
