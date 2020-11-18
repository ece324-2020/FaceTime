import cv2
import scipy.io as sio
import os
from centerface import CenterFace
import uuid
import sys

class FaceRecognition(): 
    def __init__(self, video: str,  start, end, fullpic=False):
        self.vidcap = cv2.VideoCapture(video)
        self.fullpic = fullpic
        sec = start
        frameRate = 1/2 #//it will capture image in each 0.5 second
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
        if hasFrames:
            h, w = image.shape[:2]
            landmarks = True
            centerface = CenterFace(landmarks=landmarks)
            if landmarks:
                dets, lms = centerface(image, h, w, threshold=0.35)
            else:
                dets = centerface(image, threshold=0.35)

            for det in dets:
                boxes, score = det[:4], det[4]
                x, y, dx, dy = int(boxes[0]), int(boxes[1]), int(boxes[2]), int(boxes[3])
                cropped = image[y:dy, x:dx]
                if cropped.size != 0: 
                    cv2.imwrite("crop/face" + str(count)+ '_' + str(uuid.uuid1())+".jpg", cropped)
            if self.fullpic:
                cv2.imwrite("images/image"+str(count)+".jpg", image)     # save frame as JPG file
        return hasFrames	

if __name__ == "__main__":
    from time import time
    start_time = float(sys.argv[1])
    end_time = float(sys.argv[2])
    videoName = str(sys.argv[3])
    
    print(videoName)
    # videoName = 'tbbt_s1e1.mp4'
    # start_time = 0
    # end_time = 30
    print (start_time, end_time)

    start = time()
    fr = FaceRecognition(videoName, start_time, end_time)

    print(time()-start)