import numpy as np
import cv2
import os


def cropImg(img):
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
    
    ## adjust the second and third argument 
    ret, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
    image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    con_size = [len(contours[i]) for i in range(len(contours))]
    index = con_size.index(max(con_size))
    contours = [contours[index]]
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        #print(x, y, w, h)
        #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    result = img[y:y+h, x:x+w]
    #result = cv2.cvtColor(crop, cv2.COLOR_BAYER_BG2BGRA)

    return result


def run():
    ROOT_DIR = os.getcwd()
    IMAGE_INPUT = ROOT_DIR + '/images/tick/'
    IMAGE_OUTPUT = ROOT_DIR + '/images/tick_croped/'
    file_names = next(os.walk(IMAGE_INPUT))[2]
    size = len(file_names)
    for i, file_name in enumerate(file_names):
        if file_name == ".DS_Store":
            continue
        img = cv2.imread(os.path.join(IMAGE_INPUT, file_name))
        if file_name[-4:] == '.tif':
            namePrefix = file_name.split('.tif')[0]
        elif file_name[-4:] == '.jpg':
            namePrefix = file_name.split('.jpg')[0]
        elif file_name[-4:] == '.png':
            namePrefix = file_name.split('.png')[0]
        crop = cropImg(img)
        cv2.imwrite(IMAGE_OUTPUT + namePrefix + '.png', crop)
        size -= 1
        print('Completed {}th image and left {} images'.format(i, size))



