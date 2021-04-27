import cv2

CAM_ID = 0
def showVideo(camid = CAM_ID) :
    try :
        print("카메라를 구동합니다.")
        cap = cv2.VideoCapture(camid,cv2.CAP_DSHW)
    excOept :
        print("카메라 구동 실패")
        return
    cap.set(3,480)      #카메라 속성 설정 메서드(.set(propid, value)) :propid(속성 - 카메라 설정), value(값 - 카메라 설정의 속성값)
    cap.set(4,320)
'''
    while True :
        ret, frame = cap.read()

        if not ret :
            print("비디오 읽기 오류")
            break
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video',gray)

        k = cv2.waitKey(1) 
        if k == 27 :
            break

    cap.release()
    cv2.destroyAllWindows()
'''
showVideo()