import numpy as np                                  #pip install numpy
import cv2                                          #opencv
import matplotlib.pyplot as plt                     #pip install matplotlib
from skimage.metrics import structural_similarity   #pip install scikit-image
import imutils                                      #pip install imtils

##변수선언##
testimg = ["opencv_frame_0.png", "opencv_frame_1.png"]          
edge = []
def canny(tstimg):                                  #canny edge detection으로 외곽선 추출
    img = cv2.imread(tstimg, cv2.IMREAD_GRAYSCALE)

    edge.append(cv2.Canny(img, 50, 200))            #추출한 이미지를 edge리스트에 append

    cv2.waitKey(0)
    cv2.destroyAllWindows()

##메인함수##

for i in range(0, 2):
    canny("jpg/" + testimg[i])                      #1, 2번 jpg사진 사용

diff = cv2.subtract(edge[0], edge[1])               #두 edge 사진의 차이 비교

(score, diff) = structural_similarity(edge[0], edge[1], full=True)  #두 사진의 유사성 검사.  full=true일 경우 이미지 전체를 검사.
print(diff)
##diff = (diff*255)
dif_f = diff.astype("uint8")                                   #두 사진의 차이를 diff값으로 받아 score로 유사성 계산

print(f"Similarity : {score:.5f}")                                  #유사성을 소숫점 5자리까지 프린트.  두 사진이 동일할수록 1에 가까운 수치 출력

assert score, "same"