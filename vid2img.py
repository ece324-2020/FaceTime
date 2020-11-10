import cv2
from faces import get_faces
vidcap = cv2.VideoCapture('tbbt_science.mp4')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

def getFrame(sec):
	vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
	hasFrames,image = vidcap.read()
	if hasFrames:
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 6)
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
		
		profiles = profile_cascade.detectMultiScale(gray, 1.1, 6)

		for (x, y, w, h) in profiles:
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
		img_name = "images/image"+str(count)+".jpg"
		cv2.imwrite(img_name, image)     # save frame as JPG file
		# get_faces(img_name)

	return hasFrames
sec = 500# 30*60 + 34
frameRate = 1.0/2#4.0 #0.041666 #//it will capture image in each 1/24 second
count=1
success = getFrame(sec)
print('s')
while success:
	print('h')
	count = count + 1
	sec = sec + frameRate
	# sec = round(sec, 2)
	success = getFrame(sec)
	# if count > 200:
	# 	break