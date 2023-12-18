import cv2 as cv
import numpy as np

def load_img(img_path):
    img = cv.imread(img_path, cv.IMREAD_COLOR)
    img = img.astype(np.float32)
    return img

def show_img(img, name=""):
    img = img.copy()
    img = img.astype(np.uint8)
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    img_path = "../test/example_fire.png"
    img = load_img(img_path)
    show_img(img)
