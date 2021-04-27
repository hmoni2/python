import cv2

CAM_ID = 0
def showVideo(camid = CAM_ID) :
    try :
        print("카메라를 구동합니다.")
        cap = cv2.VideoCapture(camid,cv2.CAP_DSHOW)
    except :
        print("카메라 구동 실패")
        return
    cap.set(3,480)      
    cap.set(4,320)
    #카메라 속성 설정 메서드(.set(propid, value)) :propid(속성 - 카메라 설정), value(값 - 카메라 설정의 속성값)

    while True : #웹캠이 동영상처럼 작동되게 무한 루프 돌림, 만약 while이 없는 경우 바로 종료 
    
        ret, frame = cap.read()
        if not ret :
            print("비디오 읽기 오류")
            break
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video',gray)

        k = cv2.waitKey(1)  #-1이면 입력 대기 시간 동안 아무것도 누르지 않았다는 의미 
        if k == 27 :        #esc(27)누르면 break
            break

    cv2.imwrite('test1.png',frame,params=[cv2.IMWRITE_PNG_COMPRESSION,0])
    #while문으로 사진을 캡쳐할 시에는 종료할 때의 이미지를 반환
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__' : 
    showVideo()