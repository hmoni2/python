import cv2


# Get user supplied values
imagePath = "c:\\Users\\KYOUNGAH\\python\\model.jpg"
cascPath = "haarcascade_frontalface_default.xml" ##python 폴더에 있어야함

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(       #int32
    gray,  #검출하고자 하는 원본 이미지 -> 두 번째 인자인 objects에 검출된 이미지가 채워짐
    scaleFactor=1.1, #이미지 피라미드에서 사용?? 이미지 피라미드가 뭐지? 이미지의 크기를 단계적으로 확장하거나 축소
    #검색 윈도우 확대 비율,1보다 커야함
    minNeighbors=5,#검출 영역으로 선택하기 위한 최소 검출 횟수, 얼굴 사이의 최소 간격
    minSize=(30, 30), #사이즈
    flags = cv2.CASCADE_SCALE_IMAGE #old cascade 사용시에만 의미를 가지는 파라미터
)
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
# 이미지 프레임 (x,y)부터 시작, (x+넓이, y+길이)까지의 사각형을 그림(색 0 255 0 , 굵기 2)
cv2.imshow("Faces found", image)
cv2.waitKey(0)