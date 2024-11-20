# This file was modified using OpenCV example code.

import cv2

# xml model file has to be in the same directory as this program.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('example.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(gray)

# Detect faces
faces = face_cascade.detectMultiScale(gray)
print('detected face(s) at:', faces)

# Creates Rectangle around faces
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 5)
  cv2.rectangle(img, (x-5, y-5), (x+w+5, y+h+5), (0, 0, 0), 5)

cv2.imshow('press any key to exit', img)
cv2.imwrite('example_result.jpg',img)
cv2.waitKey(0) # blocks until a key is pressed when window is active.
cv2.destroyAllWindows()
