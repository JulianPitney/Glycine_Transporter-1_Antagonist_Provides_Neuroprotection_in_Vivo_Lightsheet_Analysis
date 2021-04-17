# Glycine Transporter-1 Antagonism Induced Neuroprotection in Vivo: Lightsheet Analysis

# Table of Contents
* [Background](#background)
* [Usage](#usage)
* [Contact](#contact)
* [License](#license)

# Background
This repository contains all the material required to replicate and understand the lightsheet analysis pipeline used for the paper "Glycine Transporter-1 Antagonism Induced Neuroprotection in Vivo".

# Requirements
This guide is intended for users with basic programming skills as well as basic familiarity with scientific image analysis. Specifics are listed below.

**User Skills:**
- Basic familiarity with using command line utilities.
- Basic familiarity with Python.
- Basic familiarity with Excel.
- Basic familiarity with FIJI.  
- Ability to navigate complex GUIs (Aivia).

**Software Requirements:**

| Name | Version |
| ----------- | ----------- |
| Windows | 10 |
| Aivia | 9.0 |
| Terastitcher-portable (command-line version) | 1.11.10 |
| ImageJ (FIJI) | Most Recent |
| Excel | Most recent |
| Anaconda | 2020.11 |
| Python | 3.6.7 |
| tensorflow-gpu (optional) | 2.4.1 |
| tiff-stack-crop-tool | 0.6 |
| Pandas | 1.2.4 |
| Numpy | 1.20.2 |
| Matplotlib | 3.4.1 |


**Minimum Hardware Recommendations:**
- CPU: i9 9900k
- RAM: 64GB
- GPU: 2080ti
- Storage: 1TB

# Usage
The root directory of this repository contains 7 sub folders labeled Step[1-7]. Each subfolder contains a README detailing specifics about it's particular step in the pipeline. Each subfolder contains:

* All source code used for the step.
* Names and version numbers of all 3rd party tools used for the step.
* Background information about the purpose of the step.
* Detailed instructions for running the step, including what is required as input and what should be generated as output.
* Common troubleshooting questions and answers.
* Contact information pointing at whoever designed that step.

  **Steps:**
    1. [Tile Stitch](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/tree/master/Step1_TileStitch)
    2. [Gen Stroke Mask](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/tree/master/Step2_GenStrokeMask)
    3. [Crop Volume](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/tree/master/Step3_CropVolume)
    4. [Contrast Adjustment](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/tree/master/Step4_ContrastAdjustment)
    5. [Aivia Analysis](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/tree/master/Step5_AiviaAnalysis)
    6. [Process Aivia Results](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/tree/master/Step6_ProcessAiviaResults)
    7. [Stats Analysis](https://github.com/JulianPitney/Glycine_Transporter-1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis/tree/master/Step7_StatsAnalysis)

# Contact
* Boyang Wang (jwang149@gmail.com)
* Julia Cappelli (jcapp082@uottawa.ca)
* Junzheng Wu (alchemistWu0521@gmail.com)
* Julian Pitney (julianpitney@gmail.com)

# License
This repository is property of the Bergeron Lab and should not be distributed without explicit permission from Dr. Richard Bergeron.
