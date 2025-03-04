import cv2
import scipy.io as sio
import os
from centerface import CenterFace
import uuid
import sys
import pandas as pd

class FaceRecognition(): 
    def __init__(self, video: str,  start, end, fullpic=False):
        self.vidcap = cv2.VideoCapture(video)
        self.fullpic = fullpic
        sec = start
        frameRate = 1/2 #//it will capture image in each 0.5 second
        count=1
        d = {
            'timestamp': [],
            'filename': [] 
        }
        self.track = pd.DataFrame(data = d)
        success = self._getFrame(sec, count)
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = self._getFrame(sec, count)
            
            if sec >= end:
                self.track.to_csv('track_{}_s{}_e{}.csv'.format(video.split('.')[0], start, end), index=False)
                break
    
    def _getFrame(self, sec, count):
        self.vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = self.vidcap.read()
        names = []
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
                curruuid = uuid.uuid1()
                if cropped.size != 0: 
                    cv2.imwrite("crop/face" + str(count)+ '_' + str(curruuid)+".jpg", cropped)
                    names.append("face" + str(count)+ '_' + str(curruuid)+".jpg")
            if self.fullpic:
                cv2.imwrite("images/image"+str(count)+".jpg", image)     # save frame as JPG file
        self.track = self.track.append({
            'timestamp': float(sec), 
            'filename': names
        }, ignore_index=True)
        return hasFrames	


from time import time
start_time = float(sys.argv[1])
end_time = float(sys.argv[2])
videoName = str(sys.argv[3])
# start_time = 0
# end_time = 30
print (start_time, end_time)

start = time()
fr = FaceRecognition(videoName, start_time, end_time)

print (time()-start)