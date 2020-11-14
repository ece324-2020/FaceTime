import cv2
from faces import get_faces
import uuid

class FaceRecognition(): 
    def __init__(self, video: str, fullpic=False):
        self.vidcap = cv2.VideoCapture(video)
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
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

    def _getFrame(self, sec, count):
        self.vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = self.vidcap.read()
        if hasFrames:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cropped = image[y:y+h, x:x+h]
                if cropped.size != 0: 
                    cv2.imwrite("crop/face" + str(count)+ '_' + str(uuid.uuid1())+".jpg", cropped)
            
            profiles = self.profile_cascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in profiles:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cropped = image[y:y+h, x:x+h]
                if cropped.size != 0: 
                    cv2.imwrite("side/face" + str(count)+ '_' + str(uuid.uuid1())+".jpg", cropped)
            
            if self.fullpic:
                img_name = "images/image"+str(count)+".jpg"
                cv2.imwrite(img_name, image)     # save frame as JPG file
            # get_faces(img_name)
            # cv2.imwrite("images/image"+str(count)+".jpg", image)     # save frame as JPG file
        return hasFrames


fr = FaceRecognition('tbbt_science.mp4')