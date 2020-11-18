import cv2
from faces import get_faces
from mtcnn import MTCNN
import uuid
from rich import print
import sys

class FaceRecognition(): 
	def __init__(self, video: str, start, end, fullpic=False):
		self.vidcap = cv2.VideoCapture(video)
		self.fullpic = fullpic
		
		sec = start #0
		frameRate = 1/6
		count=1
		success = self._getFrame(sec, count)
		while success:
			count = count + 1
			sec = sec + frameRate
			sec = round(sec, 2)
			success = self._getFrame(sec, count)

			if sec >= end:
				break
	
	def _getFrame(self, sec, count):
		self.vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
		hasFrames,image = self.vidcap.read()
		detector = MTCNN()
		if hasFrames:
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			res = detector.detect_faces(image)
			for item in res:
				# itemJ = json.load(item)
				boxes = item['box']
				x, y, w, h = boxes[0], boxes[1], boxes[2], boxes[3]
				cropped = image[y:y+h, x:x+h]
				if cropped.size != 0: 
					cv2.imwrite("crop/face" + str(sec)+ '_' + str(uuid.uuid1())+".jpg", cropped)
			if self.fullpic:
				img_name = "images/image"+str(count)+".jpg"
				cv2.imwrite(img_name, image)     # save frame as JPG file
		return hasFrames

from time import time
start_time = float(sys.argv[1])
end_time = float(sys.argv[2])
print (start_time, end_time)

start = time()
fr = FaceRecognition('tbbt_science.mp4', start_time, end_time)

print (time()-start)