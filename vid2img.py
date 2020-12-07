# import cv2
# from faces import get_faces
from mtcnn import MTCNN
import cv2
import json
# from matplotlib import pyplot as plt


# # def getFrame(sec, vidcap, count):
# # 	vidcap.set(cv2.CAP_PROP_POS_MSEC,sec)
# # 	hasFrames,image = vidcap.read()
# # 	print(hasFrames)
# # 	if hasFrames:
# # 		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # 		faces = face_cascade.detectMultiScale(gray, 1.1, 6)
# # 		for (x, y, w, h) in faces:
# # 			cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
		
# # 		profiles = profile_cascade.detectMultiScale(gray, 1.1, 6)

# # 		for (x, y, w, h) in profiles:
# # 			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
# # 		img_name = "images/image"+str(count)+".jpg"
# # 		cv2.imwrite(img_name, image)     # save frame as JPG file
# # 		# get_faces(img_name)

# # 	return hasFrames

# # # def capCheck(vidcap, sec):
# # # 	vidcap.set(cv2.CAP_PROP_POS_MSEC,sec)
# # # 	ret, im = vidcap.read()
# # # 	cv2.imwrite('frame.jpg', im)
# # # 	# if cv2.waitKey(25) & 0xFF == ord('q'):
# # #     #     break

# # # 	return ret


vidcap = cv2.VideoCapture('tbbt_science.mp4')
# # # print(capCheck(vidcap, 5))

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

# # sec = 0# 30*60 + 34
# # frameRate = 5#4.0 #0.041666 #//it will capture image in each 1/24 second
# # count=1
# # success = getFrame(sec, vidcap, count)
# # print('s')
# # while success:
# # 	print('h')
# # 	count = count + 1
# # 	sec = sec + frameRate
# # 	# sec = round(sec, 2)
# # 	success = getFrame(sec, vidcap, count)
# # 	# if count > 200:
# # 	# 	break


def getFrame(sec):
	vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
	hasFrames,image = vidcap.read()
	detector = MTCNN()
	if hasFrames:
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		res = detector.detect_faces(image)
		for item in res:
			# itemJ = json.load(item)
			boxes = item['box']
			x, y, w, h = boxes[0], boxes[1], boxes[2], boxes[3]
			cropped = image[y:y+h, x:x+h]
			cv2.imwrite("crop/face" + str(count)+ ".jpg", cropped)
			cv2.imshow('')
		img_name = "images/image"+str(count)+".jpg"
		cv2.imwrite(img_name, image)     # save frame as JPG file
	return hasFrames	


def checkimg():
	image = cv2.imread('picture1.jpg')
	detector = MTCNN()
	hasFrames = True
	count = 1
	if hasFrames:
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		res = detector.detect_faces(image)
		for item in res:
			# itemJ = json.load(item)
			boxes = item['box']
			x, y, w, h = boxes[0], boxes[1], boxes[2], boxes[3]
			cropped = image[y:y+h, x:x+h]
			print(x, y, w, h)
			cv2.imwrite("crop/face" + str(count)+ ".jpg", cropped)
			cv2.imshow('crop', cropped)
		img_name = "images/image"+str(count)+".jpg"
		cv2.imwrite(img_name, image)     # save frame as JPG file
		cv2.waitKey(0)
	return hasFrames	



# sec = 0
# frameRate = 1 #//it will capture image in each 0.5 second
# count=1
# success = getFrame(sec)
# while success:
#     count = count + 1
#     sec = sec + frameRate
#     sec = round(sec, 2)
#     success = getFrame(sec)

checkimg()

