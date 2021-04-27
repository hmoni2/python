import cv2


class CannyTest() : 
    edge = []

    def CannyEdge(self,tstimg):                                  #canny edge detection으로 외곽선 추출
        img = cv2.imread(tstimg, cv2.IMREAD_GRAYSCALE)

        self.edge.append(cv2.Canny(img, 50, 200))            #추출한 이미지를 edge리스트에 append

        cv2.waitKey(0)
        cv2.destroyAllWindows()