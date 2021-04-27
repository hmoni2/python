import cv2
import numpy as np
import face_recognition
import os
import glob

# 이미지 폴더 경로, 초깃값 설정 #
path = './image'
imagepath = os.listdir(path)
imagelist = []
imglist = []
known_encodelist = []     #기존 사진 encoding 값 저장

#image 폴더에서 jpg 파일 추출
imagelist = [f for f in glob.glob(".\\image\\*.jpg")]  
#print(imagelist)
for i in imagelist :
    img = face_recognition.load_image_file(i)
    image_loc = face_recognition.face_locations(img)
    face_encoding = face_recognition.face_encodings(img)[0]
    known_encodelist.append(face_encoding)
#print(known_encodelist)
# 캠 영상 받아서 처리
cap = cv2.VideoCapture(0)

while True:
    temp, frame = cap.read()
    img_size = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    img_size = cv2.cvtColor(img_size, cv2.COLOR_BGR2RGB)

    # 캠 얼굴 인코딩
    face_Frames = face_recognition.face_locations(img_size)
    encodes_Face = face_recognition.face_encodings(img_size, face_Frames)

    # 캠 얼굴과 메모리상 인코딩 데이터간의 비교
    for encodeFace, faceLoc in zip(encodes_Face, face_Frames):
        match = face_recognition.compare_faces(known_encodelist, encodes_Face)
        distance = face_recognition.face_distance(known_encodelist, encodes_Face)
        print("match : {0} , distance : {1}".format(match,distance))
    
        matchIndex = np.argmin(distance)

        if match[matchIndex]:
            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0),2)
            cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

    cv2.imshow('cam', frame)
    key = cv2.waitKey(1)
    if key == 27 :
        break

cap.release()
cv2.destroyAllWindows()


 