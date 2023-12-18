import cv2 as cv
import numpy as np
import utils

KERNEL_SIZE = (7, 7) 

def hsv_2_hwb(hsv_img): 
    hue, saturation, value = cv.split(hsv_img)
    white = (1-saturation)*value
    black = 1-value
    hwb_img = cv.merge([hue, white, black])
    return hwb_img

def ffd(img, debug=False):
    kernel = KERNEL_SIZE
    blured_img = cv.blur(img.copy(), kernel)
    hsv_img = cv.cvtColor(blured_img.copy(), cv.COLOR_RGB2HSV)
    hsl_img = cv.cvtColor(blured_img.copy(), cv.COLOR_RGB2HLS)
    hwb_img = hsv_2_hwb(hsv_img) 
    hue, saturation, value = cv.split(hsv_img)
    _, light, _ = cv.split(hsl_img)
    _, white, black = cv.split(hwb_img)

    saturation_avg = np.average(saturation)
    black_avg = np.average(black)
    white_avg = np.average(white)
    #CC = ((hue >= 330) | (hue <= 65))
    CC = (saturation > 0.35) & (((light > 0.70) | ((black < black_avg) & (white < white_avg)) | ((white > white_avg) & (saturation > saturation_avg))) | (white >= 98) & (black <= 2))


    mask = CC.astype(np.uint8) * 255
    if debug:
        mask_colored = cv.merge([mask, mask, mask])
        result = cv.bitwise_and(img.astype(np.uint8), mask_colored)
        #utils.show_img(mask) 
        #utils.show_img(img) 
        utils.show_img(result)
    return mask 

if __name__ == "__main__":
    img_path = "../test/RGB_Img_complete_100/379_rgb.png"
    img = utils.load_img(img_path)
    ffd(img)
