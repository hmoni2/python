import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('c:\\Users\\KYOUNGAH\\python\\JPG\\picture1.jpg') 

kernel = np.ones((5,5), np.float32) / 25        ##필터 행령 생성,25로 나누어 주는 이유는 정규화 해주기 위함
# 그러기 위해서 mask의 모든 배열의 값을 더한 다음 역수로 만들어서 곱해줌\ 
blur = cv2.filter2D(img, -1, kernel)             ##필터 적용하여 이미지 반환

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()