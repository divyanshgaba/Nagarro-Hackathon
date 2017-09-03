from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
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
from flask import jsonify
app = FlaskAPI(__name__)

data = dataset.read_train_sets(train_path, img_size, classes, validation_size=validation_size)

obj = Model()
session = tf.Session()
session.run(tf.global_variables_initializer())
saver = tf.train.Saver()
saver.restore(session,"data/model/model.ckpt")

@app.route("/", methods=['GET'])
def notes_list():
    """
    List or create notes.
    """
    return "usage: http://10.177.12.164:5000/<int:id>/"


@app.route("/<int:key>/", methods=['GET'])
def notes_detail(key):

    if key >= len(data.train.labels ) + len(data.train.labels):
        return ""
    images = []
    labels = []
    ids = []
    if(key < len(data.train.labels)):
        images = data.train.images[key:key+1].reshape(1,img_size_flat)
        labels = data.train.labels[key:key+1]
    else:
        key -=len(data.train.labels)
        images = data.valid.images[key:key+1].reshape(1,img_size_flat)
        labels = data.valid.images[key:key+1]

    feed_dict = {obj.x:images,
                 obj.y_true: labels}

    cls_pred = session.run(obj.y_pred_cls,feed_dict= feed_dict)
    cls = (classes[cls_pred[0]])
    if cls in ['paper','plastic','metal','cardboard']:
        return jsonify({"type":"blue" })
    else:
        return jsonify({"type":"green" })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
