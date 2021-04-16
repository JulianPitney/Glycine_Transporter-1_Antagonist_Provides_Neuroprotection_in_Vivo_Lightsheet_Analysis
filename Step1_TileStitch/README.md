# Step 1: Tile Stitch

This step is where Terastitcher is used to combine the component tiles of a lightsheet scan into a single tile. A complex set of algorithms are used to align and blend the tiles as accurately as possible. For more information on this topic see Terastitcher's GitHub page here -> (http://abria.github.io/TeraStitcher/)

# Table of Contents
* [Purpose](#purpose)
* [Usage](#usage)
* [Troubleshooting](#troulbeshooting)
* [Contact](#contact)

# Purpose
Since our samples were whole brains, our objective lens and image detector were not large enough to image the entire sample with a single stack. Because of this, we split the sample acquisition into multiple "tiles". The first step of processing a scan is to stitch all it's tiles into a single large tile.
# Usage
The terastitch.py script in this repository takes a directory of tiled lightsheet scans as input. It then stitches each of those sets of tiles into a single scan. It will loop over every scan in the directory until they've all been stitched.

**Requirements:**

| Name | Version |
| ----------- | ----------- |
| Windows | 10 |
| Terastitcher-portable (command-line version) | 1.11.10 |
| Python | 3.6.7 |

**Inputs:** A directory of tiled lightsheet scans following the directory structure outlined by TeraStitcher's documentation.

**Outputs:** A single stitched scan for each set of tiles supplied as input.

**Steps:**

1. Download Terastitcher-portable (command-line version) from TeraStitcher's GitHub page -> (https://github.com/abria/TeraStitcher/wiki/Binary-packages)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Version: `TeraStitcher-portable-1.11.10-win64`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Once downloaded and extracted, add `~\TeraStitcher-portable-1.11.10-win64\` to your windows system path.  

2. Depending on your scan acquisition settings, you may need to edit the configuration of Terastitcher. If you're using the scans published with this paper, the default settings are correct. If not, open `terastitch.py`and edit the variables listed below to match your settings.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Definitions for these variables can be found in Terastitcher's documentation here:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(https://github.com/abria/TeraStitcher/wiki/User-Interface#-command-line-interface-cli)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ref1, ref2, ref3, vxl1, vxl2, vxl3, imin_regex, imin_plugin, volin_plugin, oH, oV, sH, sV, sD]


3. From the command line, navigate to the directory where you've placed all your lightsheet scans (make sure the scans have the directory/file structure specified by Terastitcher's documentation or it will not work. Our lightsheet microscope spits our scans out in this format by default so no modification should be needed). From this directory, run the `terastitch.py` file supplied by this repository.

- E.G `cd ~\path-to-my-scans\ && python ~\Glycine_Transporter-            1_Antagonism_Induced_Neuroprotection_in_Vivo_Lightsheet_Analysis\Step1_TileStitch\terastitch.py`

4. If everything worked correctly, the program should begin looping over your scans and stitching them together until they're all stitched. The stitched scans will be inside a directory called `stitched` that's been placed inside each scan's folder.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Note:** This is completely CPU bound and could take many hours if you have many large scans.

# Troubleshooting

No common problems reported yet.
# Contact
* [Julian Pitney](www.julianpitney.com)
