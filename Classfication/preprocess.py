import os
import numpy
import opencv
import scipy
import constants

datapath = os.path.join(os.getcwd(),'data')
prepath = os.path.join(datapath, 'resized')
postpath = os.path.join(datapath, 'preprocessed')
labelpath = os.path.join(datapath, 'label')

if not os.path.exists(datapath):
    os.makedirs(datapath)
    
if not os.path.exists(datapath):
    os.makedirs(prepath)
    
if not os.path.exists(datapath):
    os.makedirs(postpath)
    
if not os.path.exists(datapath):
    os.makedirs(labelpath)


def process(csv_f):
    

csv_f = open(os.path.join(labelpath, 'train.csv'), 'a+')
process(csv_f)
csv_f.close()
