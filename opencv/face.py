import face_recognition
import cv2
from PIL import Image

image = face_recognition.load_image_file('model.jpg')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

face_recognition.face_encodings