import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny() :
    fName = 'JPG\\picture1.jpg'
    img = cv2.imread(fName,cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img,100,255)
    edge2 = cv2.Canny(img,150,255)
    edge3 = cv2.Canny(img,200,255)

    cv2.imshow('original', img)
    cv2.imshow('Canny Edge1', edge1)
    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()