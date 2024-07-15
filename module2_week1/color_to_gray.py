import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread('module2_week1\dog.jpg')

def color2gray_lightness(vector):
    result = (np.max(vector) + np.min(vector)) / 2
    return result


def color2gray_average(vector):
    return vector.mean()


def color2gray_luminosity(vector):
    result = 0.21 * vector[0] + 0.72 * vector[1] + 0.07 * vector[2]
    return result


gray_img_01 = np.apply_along_axis(color2gray_lightness, axis=2, arr=img)
print(gray_img_01[0, 0])

gray_img_02 = np.apply_along_axis(color2gray_average, axis=2, arr=img)
print(gray_img_02[0, 0])

gray_img_03 = np.apply_along_axis(color2gray_luminosity, axis=2, arr=img)
print(gray_img_03[0, 0])