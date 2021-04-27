import cv2
import numpy as np
import face_recognition

#이미지 로드 #
harry = face_recognition.load_image_file("C:\\Users\\KYOUNGAH\\python\\image\\harry.jpg")
comp_harry = face_recognition.load_image_file("C:\\Users\\KYOUNGAH\\python\\image\\harry2.jpg")
her = face_recognition.load_image_file("C:\\Users\\KYOUNGAH\\python\\image\\hermione.jpg")


harry_gray = cv2.cvtColor(harry,cv2.COLOR_BGR2RGB)
comh_gray = cv2.cvtColor(comp_harry,cv2.COLOR_BGR2RGB)
her_gray = cv2.cvtColor(her,cv2.COLOR_BGR2RGB)

#이미지 분석 #
harry_face = face_recognition.face_locations(harry)[0]
encode_harry = face_recognition.face_encodings(harry_gray)[0]

comh_face = face_recognition.face_locations(comp_harry)[0]
encode_comh = face_recognition.face_encodings(comh_gray)[0]

her_face = face_recognition.face_locations(her)[0]
encode_her = face_recognition.face_encodings(her_gray)[0] 

cv2.rectangle(harry,(harry_face[3],harry_face[0]),(harry_face[1],harry_face[2]),(0,255,0),2)
cv2.rectangle(comp_harry,(comh_face[3],comh_face[0]),(comh_face[1],comh_face[2]),(0,255,0),2)
cv2.rectangle(her,(her_face[3],her_face[0]),(her_face[1],her_face[2]),(0,255,0),2)

#일치 결과 비교 #
harry_result = face_recognition.compare_faces([encode_harry],encode_comh)
harry_result1 = face_recognition.face_distance([encode_harry],encode_comh)
print(harry_result1)
index = np.argmin(harry_result1)
print(index)
her_result = face_recognition.compare_faces([encode_harry],encode_her)
print("harry is harry : {0} or her is harry : {1}".format(harry_result, her_result))

#이미지 출력 #
cv2.imshow('harry',harry)
cv2.imshow('comp_harry',comp_harry)
cv2.imshow('hermione',her)
cv2.waitKey(0)