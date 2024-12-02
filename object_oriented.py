class facefinder:
	'''this is going to use haar cascade as filter to detect the largest face'''




"-------------------------------------"
## main code
ff = facefinder()
# create cam
cap = cv2.VideoCapture(cv2.CAP_ANY)
if not cap.isOpened():
	print("Couldnt open cam")
	exit()





While True:
	retval, frame = cap.read()
	if retval == False:
		print("camera error!")

	ff.find_face(frame)
	cv2.imshow('q to quit', frame)

	if cv2.waitKey(30) == ord('q'):
		break




# pause = input('press enter to end')

# destroy cam