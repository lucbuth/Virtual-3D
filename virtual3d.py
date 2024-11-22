import cv2 as cv
import numpy as np

print('Launching virtual3d.')

# make sure the xml model file is in same directory as this program.
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    #   detectMultScale returns an 2d ndarray
    faces = face_cascade.detectMultiScale(gray)
    print('detected face(s) at:', faces)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
      cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)
      cv.rectangle(frame, (x-5, y-5), (x+w+5, y+h+5), (0, 0, 0), 5)


    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
print('virtual3d complete.')
