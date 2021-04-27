import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('c:\\Users\\KYOUNGAH\\python\\JPG\\picture1.jpg')
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()