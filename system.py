import cv2
from pathlib import Path

class System: 
    def __init__(self, video, vidbreak: int, actorlist: list, \
                imagedir: str, modeldir: str):
        self.vidcap = video
        self.imagedir = Path(imagedir)
        self.modeldir = Path(modeldir)
        self.actorlist = actorlist
        self.vidbreak = vidbreak
        self.prob = {}
        self.minutes = {}
        for actor in self.actorlist:
            prob[actor] = 0
            minutes[actor] = 0
        self.times = list()
        self.times.extend(self.imagedir.iterdir())
        
        for currtime in self.times:
            images = self._load_images(currtime)
            for model in self.modeldir.iterdir():
                #add the 

    def _load_images(self, currtime):
        images = []
        for im in currtime.iteridr():
            self.images.append(cv2.imread(str(im))
        return images
        

