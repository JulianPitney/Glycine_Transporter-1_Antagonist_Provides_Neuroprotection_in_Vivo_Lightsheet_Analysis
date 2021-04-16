"""Console script for tiff_stack_crop_tool."""
import argparse
import sys
from tiff_stack_crop_tool.tiff_stack_crop_tool import crop_all_stacks


def main():
    """Console script for tiff_stack_crop_tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--scans_dir', metavar='<scans_dir>', dest='SCANS_DIR', action='store', required=True,
                        help='Full path to directory where scan tiff stacks are. This directory should ONLY contain '
                             'scan tiff stacks.')
    parser.add_argument('--masks_dir', metavar='<scans_dir>', dest='MASKS_DIR', action='store', required=False,
                        help='Full path to directory where stroke masks are. Stroke masks should be 8-bit grayscale '
                             'tiff stacks with the .tif extension. There should be one stroke mask for each scan in t'
                             'he <scans_dir> directory and this pairing should have identical ZYX dimensions. The str'
                             'oke mask tiffs should be named following this example: If <scans_dir> has a file called'
                             'scan1.tif, the corresponding stroke mask should be named scan1_stroke_mask.tif')
    parser.add_argument('--W', metavar='<INIT_W', dest='INIT_W', action='store', required=True,
                        help='An integer value representing the width of the cropping box.')

    parser.add_argument('--H', metavar='<INIT_H', dest='INIT_H', action='store', required=True,
                        help='An integer value representing the height of the cropping box.')

    args = vars(parser.parse_args())
    crop_all_stacks(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
