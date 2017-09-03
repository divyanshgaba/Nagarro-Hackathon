import csv
import os
import sys
import glob
datapath = os.path.join(os.getcwd(),'data')
path= os.path.join(datapath,'train')
path = os.path.join(path,'cardboard')
print(path)
files = glob.glob(path)
print(files)
