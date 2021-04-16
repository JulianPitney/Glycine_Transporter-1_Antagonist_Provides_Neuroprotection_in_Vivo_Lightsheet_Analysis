import os

scans = os.listdir(path='.')
inputDir = os.getcwd()

for scan in scans:

    if os.path.isdir(scan):

        # Step 1 (Import)
        volumePath = scan
        ref1 = "\"x\""
        ref2 = "\"y\""
        ref3 = "\"z\""
        vxl1 = "\"1.43\""
        vxl2 = "\"1.43\""
        vxl3 = "\"5.0\""
        imin_regex = "\"000000.tif\""
        imin_plugin = "\"tiff3D\""
        volin_plugin = "\"TiledXY|3Dseries\""
        command = "terastitcher --import --volin=" + volumePath + " --ref1=" + ref1 + " --ref2=" + ref2 + " --ref3=" + ref3 + " --vxl1=" + vxl1 \
                    + " --vxl2=" + vxl2 + " --vxl3=" + vxl3 + " --volin_plugin=" + volin_plugin + " --imin_regex=" + imin_regex + " --imin_plugin=" + imin_plugin
        os.system(command)
        print(command)

        # Step 2 (Align)
        projin = "\"" + volumePath + "\\xml_import.xml\""
        oH = "\"245\""
        oV = "\"205\""
        sH = "\"99\""
        sV = "\"99\""
        sD = "\"99\""
        command = "terastitcher --displcompute --projin=" + projin + " --oH=" + oH + " --oV=" + oV + " --sH=" + sH + " --sV=" + sV + " --sD=" + sD
        os.system(command)
        print(command)

        # Step 3 (Project)
        projin = "\"" + volumePath + "\\xml_displcomp.xml\""
        command = "terastitcher --displproj --projin=" + projin
        os.system(command)
        print(command)

        # Step 4 (Threshold)
        projin = "\"" + volumePath + "\\xml_displproj.xml\""
        threshold = "\"0.7\""
        command = "terastitcher --displthres --projin=" + projin + " --threshold=" + threshold
        os.system(command)
        print(command)

        # Step 5 (Place)
        projin = "\"" + volumePath + "\\xml_displthres.xml\""
        command = "terastitcher --placetiles --projin=" + projin
        os.system(command)
        print(command)

        # Step 6 (Merge)
        projin = "\"" + volumePath + "\\xml_merging.xml\""
        print(volumePath)
        os.mkdir(volumePath + "\\stitched")
        volout = "\"" + volumePath + "\\stitched\""
        volout_plugin = "\"TiledXY|3Dseries\""
        imout_format = "\"tif\""
        resolution = "\"1\""
        command = "terastitcher --merge --projin=" + projin + " --volout=" + volout + " --volout_plugin=" + volout_plugin + " --imout_format=" + imout_format + " --resolutions=" + resolution
        os.system(command)
        print(command)
