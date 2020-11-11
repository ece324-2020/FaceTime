import cv2
from pathlib import Path
import torch

class System: 
    def __init__(self, video, vidbreak: int, actorlist: list, \
                imagedir: str, modeldir: str):
        self.vidcap = video
        self.imagedir = Path(imagedir)
        self.modeldir = Path(modeldir)
        self.actorlist = actorlist
        # self.vidbreak = vidbreak
        self.minutes = {}
        for actor in self.actorlist:
            minutes[actor] = 0
        self.times = list()
        self.times.extend(self.imagedir.iterdir())
        
        for currtime in self.times: #each folder will be in a time stamp
            images = self._load_images(currtime)
            for pt in self.modeldir.iterdir(): #only one output from this iteration -> which prob is highest 
                # self._reset_prob()
                maxprob = (None, None)
                model = torch.load(str(pt))
                for im in images: #images is a posix directory
                    #todo: add this later
                    break
                    #self.prob[actor/model] = model(im)
                    #one model -> one actor so each model 
                    currprob = model(str(im))
                    if currprob > maxprob[0]: 
                        maxprob[0] = currprob
                        maxprob[1] = str(model)
            actorTime = self.minutes[maxprob[1] #some stupid immutability with python dicts lmao
            self.minutes[maxprob[1]] = actorTime + int(currtime)

    def _load_images(self, currtime):
        images = []
        for im in currtime.iteridr():
            images.append(cv2.imread(str(im)))
        return images
        
    # def _reset_prob(self):
    #     self.prob = {}
    #     for actor in self.actorlist:
    #         prob[actor] = 0
