import cv2
import tifffile as tif
import numpy as np
from os import remove




def load_stack(path):
    return tif.imread(path)

def save_stack(stack):

    for z in range(0, len(stack)):
        cv2.imwrite("../packages/" + str(z) + ".png", stack[z])

def save_png(path, image):
    cv2.imwrite(path, image)

def gen_stack_dims_dict(stack):
    return dict({'z': stack.shape[0], 'y': stack.shape[1], 'x': stack.shape[2]})

def max_project(stack):

    stackMax = np.max(stack, axis=0)
    return stackMax

def max_project_x(stack):

    stackMax = np.max(stack, axis=2)
    return stackMax

def max_project_y(stack):

    stackMax = np.max(stack, axis=1)
    return stackMax


def save_and_reload_maxproj(stack):

    max = max_project(stack)
    cv2.imwrite("temp.jpg", max)
    max = cv2.imread("temp.jpg")
    remove('temp.jpg')
    return max

def save_and_reload_maxproj_x(stack):

    max = max_project_x(stack)
    cv2.imwrite("temp.jpg", max)
    max = cv2.imread("temp.jpg")
    remove('temp.jpg')
    return max

def display_stack(stack, auto):

    cv2.namedWindow('stack', cv2.WINDOW_NORMAL)

    for slice in stack:

        cv2.imshow('stack', slice)

        if auto:
            cv2.waitKey(1)
        else:
            cv2.waitKey(0)

def convert_grayscale_stack_to_color(stack):

    color_stack = np.stack((stack,)*3, axis=-1)
    return color_stack

def color_map(stackGray, stackColor):

    for z in range(0, len(stackGray)):
        stackColor[z] = cv2.applyColorMap(stackGray[z], 2)



# In-place binary thresholding of a stack.
# Note: Threshold should be obtained from histogram info
# (either manual inspection or automatic)
def remove_all_pixels_below_threshold(stack, threshold):

    print("remove_all_pixels_below_threshold(): Starting...")

    for z in range(0, len(stack)):
        ret, thresholded_slice = cv2.threshold(stack[z], threshold, 255, cv2.THRESH_TOZERO)
        stack[z] = thresholded_slice

    print("remove_all_pixels_below_threshold(): Completed!")




def kernel_filter_2d(stack, kernelDims):

    print("kernel_filter_2d(): Starting...")
    kernel = np.ones(kernelDims, np.float32) / (kernelDims[0] * kernelDims[1])

    for z in range(0, len(stack)):
        stack[z] = cv2.filter2D(stack[z], -1, kernel)
    print("kernel_filter_2d(): Completed!")


def save_and_reload_maxproj(stack):

    max = max_project(stack)
    cv2.imwrite("temp.jpg", max)
    max = cv2.imread("temp.jpg")
    remove('temp.jpg')
    return max

def save_and_reload_maxproj_x(stack):

    max = max_project_x(stack)
    cv2.imwrite("temp.jpg", max)
    max = cv2.imread("temp.jpg")
    remove('temp.jpg')
    return max

def save_and_reload_maxproj_y(stack):

    max = max_project_y(stack)
    cv2.imwrite("temp.jpg", max)
    max = cv2.imread("temp.jpg")
    remove('temp.jpg')
    return max


def gen_stack_dims_dict(stack):

    return dict({'z': stack.shape[0], 'y': stack.shape[1], 'x': stack.shape[2]})

def print_crop_dims(stackDimsDict):

    print("Cropped Dimensions:")
    print("zDim=" + str(stackDimsDict['z']))
    print("yDim=" + str(stackDimsDict['y']))
    print("xDim=" + str(stackDimsDict['x']))