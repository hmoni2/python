import cv2
import time

# 초기 설정
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,480)
cap.set(4,320)
cascPath = "haarcascade_frontalface_default.xml" ##python 폴더에 있어야함
faceCascade = cv2.CascadeClassifier(cascPath)


#이미지 읽기
#image = cv2.imread(imagepath)
start_time = time.time()
count = 0   #웹캠 사진 찍어서 이미지 저장

while True : 
    ret,frame = cap.read()
    
    if not ret :
        print("비디오 읽기 오류 ")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(     #크기가 다른 오브젝트 검출   
        gray,  
        scaleFactor=1.1, 
        minNeighbors=5,
        minSize=(10, 10), 
        flags = cv2.CASCADE_SCALE_IMAGE 
    )

    # 이미지 프레임 (x,y)부터 시작, (x+넓이, y+길이)까지의 사각형을 그림(색 0 255 0 , 굵기 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
    cv2.imshow("video show", frame)
    key = cv2.waitKey(1)
    if key == 27 :
        break

     # 1초 마다 사진 찍게 
    if time.time() - start_time  >= 1 :  
        img_name = "opencv_frame_{}.png".format(count)
        cv2.imwrite(img_name,frame,params=[cv2.IMWRITE_PNG_COMPRESSION,0])
        print("{0} written".format(count))
        start_time = time.time()
        count += 1
    
cap.release()
cv2.destroyAllWindow()