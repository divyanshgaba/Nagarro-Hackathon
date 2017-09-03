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
from constants import *

class Model():
    def new_weights(shape):
        return tf.Variable(tf.truncated_normal(shape, stddev=0.05))
    def new_biases(length):
        return tf.Variable(tf.constant(0.05, shape=[length]))

    def new_conv_layer(input,              
                       num_input_channels, 
                       filter_size,
                       num_filters,        
                       use_pooling=True):  


        shape = [filter_size, filter_size, num_input_channels, num_filters]

        weights = Model.new_weights(shape=shape)

        biases = Model.new_biases(length=num_filters)

        layer = tf.nn.conv2d(input=input,
                             filter=weights,
                             strides=[1, 1, 1, 1],
                             padding='SAME')

        layer += biases

        if use_pooling:
            layer = tf.nn.max_pool(value=layer,
                                   ksize=[1, 2, 2, 1],
                                   strides=[1, 2, 2, 1],
                                   padding='SAME')

        layer = tf.nn.relu(layer)

        return layer, weights

    def flatten_layer(layer):
        layer_shape = layer.get_shape()


        num_features = layer_shape[1:4].num_elements()

        layer_flat = tf.reshape(layer, [-1, num_features])

        return layer_flat, num_features
    def new_fc_layer(input,         
                     num_inputs,
                     num_outputs,
                     use_relu=True): 

        weights = Model.new_weights(shape=[num_inputs, num_outputs])
        biases = Model.new_biases(length=num_outputs)

        layer = tf.matmul(input, weights) + biases

        # Use ReLU?
        if use_relu:
            layer = tf.nn.relu(layer)

        return layer

    def __init__(self):
        self.x = tf.placeholder(tf.float32,shape = [None,img_size_flat],name = 'x')
        self.x_image = tf.reshape(self.x,[-1,img_size,img_size,num_channels])

        self.y_true = tf.placeholder(tf.float32,shape =[None,num_classes],name='y_true')

        self.y_true_cls = tf.argmax(self.y_true,dimension=1)

        layer_conv1, weight_conv1 = \
            Model.new_conv_layer(input=self.x_image,
                                    num_input_channels=num_channels,
                                    filter_size=filter_size1,
                                    num_filters=num_filters1,
                                    use_pooling=True)

        #print(layer_conv1)
        layer_conv2, weight_conv2 = \
            Model.new_conv_layer(input=layer_conv1,
                                    num_input_channels=num_filters1,
                                    filter_size=filter_size2,
                                    num_filters=num_filters2,
                                    use_pooling=True)
        #print(layer_conv2)
        layer_conv3, weights_conv3 = \
            Model.new_conv_layer(input=layer_conv2,
                           num_input_channels=num_filters2,
                           filter_size=filter_size3,
                           num_filters=num_filters3,
                           use_pooling=True)
        layer_flat, num_features = Model.flatten_layer(layer_conv2)

        #print(layer_flat)
        #print(num_features)

        layer_fc1 = Model.new_fc_layer(input=layer_flat,
                                 num_inputs=num_features,
                                 num_outputs=fc_size,
                                 use_relu=True)
        #print(layer_fc1)
        self.layer_fc2 = Model.new_fc_layer(input=layer_fc1,
                                 num_inputs=fc_size,
                                 num_outputs=num_classes,
                                 use_relu=False)
        #print(layer_fc2)
        self.y_pred = tf.nn.softmax(self.layer_fc2)
        self.y_pred_cls = tf.argmax(self.y_pred,dimension=1)
