import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix
import time
from datetime import timedelta
import math
import pandas as pd
import dataset
import random
from model import *
from constants import *


data = dataset.read_train_sets(train_path, img_size, classes, validation_size=validation_size)

obj = Model()

session = tf.Session()
session.run(tf.global_variables_initializer())

saver = tf.train.Saver()
saver.restore(session,"data/model/model.ckpt")


images = data.valid.images[0:1].reshape(1,img_size_flat)
labels = data.valid.labels[0:1]
feed_dict = {obj.x:images,
             obj.y_true: labels}

cls_pred = session.run(obj.y_pred_cls,feed_dict= feed_dict)
print(classes[cls_pred[0]])




        
