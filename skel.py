import cv2
import numpy as np
import os
def convert(image):
    img = cv2.imread(image,0)
    size = np.size(img)
    skel = np.zeros(img.shape,np.uint8)
    
    ret,img = cv2.threshold(img,127,255,0)


    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
    
    while( not done):
        eroded = cv2.erode(img,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(img,temp)
        skel = cv2.bitwise_or(skel,temp)
        img = eroded.copy()
    
        zeros = size - cv2.countNonZero(img)
        if zeros==size:
            done = True
    name=str(os.path.join('static/images'))+'/converted_'+str(image.split('/')[-1])
    cv2.imwrite(name, skel)
    # cv2.imshow("skel",skel)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()