import cv2
import scipy.io as sio
import os
from centerface import CenterFace

class FaceRecognition(): 
    def __init__(self, video: str, fullpic=False):
        self.vidcap = cv2.VideoCapture(video)
        self.fullpic = fullpic
        sec = 0
        frameRate = 1 #//it will capture image in each 0.5 second
        count=1
        success = self._getFrame(sec, count)
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = self._getFrame(sec, count)
    
    def _getFrame(sec, count):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
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
                cv2.imwrite("crop/face" + str(count)+ ".jpg", cropped)
            if self.fullpic:
                cv2.imwrite("images/image"+str(count)+".jpg", image)     # save frame as JPG file
        return hasFrames	


fr = FaceRecognition('tbbt_science.mp4')