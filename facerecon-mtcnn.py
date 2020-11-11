import cv2
from faces import get_faces
from mtcnn import MTCNN

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
                cv2.imwrite("crop/face" + str(count)+ ".jpg", cropped)
            if self.fullpic:
                img_name = "images/image"+str(count)+".jpg"
                cv2.imwrite(img_name, image)     # save frame as JPG file
        return hasFrames


fr = FaceRecognition('tbbt_science.mp4')