import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils, datasets
from torch.utils.data.sampler import SubsetRandomSampler

'''
THIS DOES NOT INHERIT FROM THE DATALOADER CLASS! YOU CAN JUST INSTANTIATE AND CALL THE TRAIN, TEST AND VALID

datasetobject = FacialRecognitialDataset()
trainData = datasetobject.train
validData = datasetobject.valid
testData = datasetobject.test
 
'''
class FacialRecognitialDataset:
    def __init__(self, transformation = None, root='.', validSize=0.2, trainSize=0.7, testSize=0.1,
                 randomSeed=100, shuffle=True, num_workers=4, batchSize=64):
        
        _loadFullDataset(firstRun=True)
        miu, sig = _getMeanStd()
        _loadFullDataset(miu=miu, sig=sig, firstRun=False)
        _loadData(validSize, trainSize, testSize, randomSeed, batchSize, num_workers)
        
    def _getMeanStd(self):
        nimages = 0
        mean = 0.
        std = 0.
        for batch, _ in self.fulldataset:
            # Rearrange batch to be the shape of [B, C, W * H]
            batch = batch.view(batch.size(0), batch.size(1), -1)
            # Update total number of images
            nimages += batch.size(0)
            
            # Compute mean and std here
            mean += batch.mean(2).sum(0) 
            std += batch.std(2).sum(0)
        mean /= nimages
        std /= nimages

        return mean, std

    def _loadFullDataset(self, miu=None, sig=None, firstRun=False, transformation, 
                         num_workers):
        if firstRun==False:
            self.transform = transforms.Compose([
                                transforms.Resize(255),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize((miu[0], miu[1], miu[2]), (sig[0], sig[1], sig[2]))])
        else:
            self.transform = None
        self.fulldataset = datasets.ImageFolder(root=root, transform = self.transform)
        
    def _loadData(self, validSize, trainSize, testSize, randomSeed, batchSize):
        num = len(self.fulldataset)
        indices = list(range(num))
        split = int(np.floor(validSize * num))
        testSplit = int(np.floor(testSize*num))
        
        #doesn't really matter since we use subsetrandomsampler lol
        np.random.seed(randomSeed)
        np.random.shuffle(indices)
        
        validIdx, testIdx, trainIdx = indices[:split], indices[split:testSplit], indices[testSplit:]
        trainSample = SubsetRandomSampler(trainIdx)
        validSample = SubsetRandomSampler(validIdx)
        testSample = SubsetRandomSampler(testIdx)
        
        self.train = utils.data.DataLoader(
            self.fulldataset, batch_size=batchSize, sampler=trainSample, num_workers=num_workers
        )
        self.valid = utils.data.DataLoader(
            self.fulldataset, batch_size=batchSize, sampler=validSample, num_workers=num_workers
        )
        self.test = utils.data.DataLoader(
            self.fulldataset, batch_size=batchSize, sampler=testSample, num_workers=num_workers
        )
        
        
        
        