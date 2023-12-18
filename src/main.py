from forest_fire_detection import ffd
import cv2 as cv
import utils

if __name__ == "__main__":
    img_path = "../test/RGB_Img_complete_100/379_rgb.png"
    img = utils.load_img(img_path)
    mask = ffd(img, debug=True)
    cv.imwrite("mask.png", mask)
