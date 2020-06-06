import cv2

imagePath = "img.jpg"
cascPath = "fd.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
cap=cv2.VideoCapture(0)
#image = cv2.imread(imagePath)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image

while(1):
    ret,frame=cap.read()
    imgray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print("Found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Faces found", frame)
#cv2.resizeWindow('Faces found',640,480);
#while(1):
    if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()

