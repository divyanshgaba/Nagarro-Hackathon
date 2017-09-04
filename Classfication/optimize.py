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
from model import *

data = dataset.read_train_sets(train_path, img_size, classes, validation_size=validation_size)
print("Size of:")
print("- Training-set:\t\t{}".format(len(data.train.labels)))
print("- Test-set:\t{}".format(len(data.valid.labels)))




def plot_images(images, cls_true, cls_pred=None):
    
    if len(images) == 0:
        print("no images to show")
        return 
    else:
        random_indices = random.sample(range(len(images)), min(len(images), 9))
        
        
    images, cls_true  = zip(*[(images[i], cls_true[i]) for i in random_indices])
    
    fig, axes = plt.subplots(3, 3)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i].reshape(img_size, img_size, num_channels))

        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

        ax.set_xlabel(xlabel)
        
        ax.set_xticks([])
        ax.set_yticks([])
    
    plt.show()

    
'''
images = data.test.images[0:9]
cls_true = data.test.cls[0:9]
plot_images(images=images,cls_true=cls_true)
'''

model = Model()
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=model.layer_fc2,
                                                        labels=model.y_true)
cost = tf.reduce_mean(cross_entropy)

optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)

correct_prediction = tf.equal(model.y_pred_cls,model.y_true_cls)

accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

session = tf.Session()

session.run(tf.global_variables_initializer())

saver = tf.train.Saver()
#saver.restore(session,"data/model/model.ckpt")

train_batch_size = 4

def print_progress(epoch, feed_dict_train, feed_dict_validate, val_loss):
    acc = session.run(accuracy, feed_dict=feed_dict_train)
    val_acc = session.run(accuracy, feed_dict=feed_dict_validate)
    msg = "Epoch {0} --- Training Accuracy: {1:>6.1%}, Validation Accuracy: {2:>6.1%}, Validation Loss: {3:.3f}"
    print(msg.format(epoch + 1, acc, val_acc, val_loss))
    
total_iterations = 0

def optimize(num_iterations):
    global total_iterations

    start_time = time.time()
    
    best_val_loss = float("inf")
    patience = 0

    for i in range(total_iterations,
                   total_iterations + num_iterations):


        x_batch, y_true_batch, _, cls_batch = data.train.next_batch(train_batch_size)
        x_valid_batch, y_valid_batch, _, valid_cls_batch = data.valid.next_batch(train_batch_size)



        x_batch = x_batch.reshape(train_batch_size, img_size_flat)
        x_valid_batch = x_valid_batch.reshape(train_batch_size, img_size_flat)


        feed_dict_train = {model.x: x_batch,
                           model.y_true: y_true_batch}
        
        feed_dict_validate = {model.x: x_valid_batch,
                              model.y_true: y_valid_batch}


        session.run(optimizer, feed_dict=feed_dict_train)
        

        if i % int(data.train.num_examples/batch_size) == 0: 
            val_loss = session.run(cost, feed_dict=feed_dict_validate)
            epoch = int(i / int(data.train.num_examples/batch_size))
            
            print_progress(epoch, feed_dict_train, feed_dict_validate, val_loss)
            
            if early_stopping:    
                if val_loss < best_val_loss:
                    best_val_loss = val_loss
                    patience = 0
                else:
                    patience += 1

                if patience == early_stopping:
                    break

    total_iterations += num_iterations

    end_time = time.time()

    time_dif = end_time - start_time

    print("Time elapsed: " + str(timedelta(seconds=int(round(time_dif)))))



batch_size = 4
    
def print_validation_accuracy(show_example_errors=False,
                        show_confusion_matrix=False):


    num_test = len(data.valid.images)


    cls_pred = np.zeros(shape=num_test, dtype=np.int)


    i = 0

    while i < num_test:
        j = min(i + batch_size, num_test)

        images = data.valid.images[i:j, :].reshape(batch_size, img_size_flat)
        

        labels = data.valid.labels[i:j, :]

        feed_dict = {model.x: images,
                     model.y_true: labels}

        cls_pred[i:j] = session.run(model.y_pred_cls, feed_dict=feed_dict)


        i = j

    cls_true = np.array(data.valid.cls)
    cls_pred = np.array([classes[x] for x in cls_pred]) 

    correct = (cls_true == cls_pred)


    correct_sum = correct.sum()


    acc = float(correct_sum) / num_test

    msg = "Accuracy on Test-Set: {0:.1%} ({1} / {2})"
    print(msg.format(acc, correct_sum, num_test))

optimize(num_iterations=1)
print_validation_accuracy()
#saver.save(session,"data/model/model.ckpt")
#print_test_accuracy(show_example_errors=True,show_confusion_matrix=False)
images = data.valid.images[0:4].reshape(4,img_size_flat)
labels = data.valid.labels[0:4]
feed_dict = {model.x:images,
             model.y_true: labels}

cls_pred = session.run(model.y_pred_cls,feed_dict= feed_dict)
print(cls_pred)


'''''
y_predicted = session.run(y_pred_cls, feed_dict= {data.valid.images[0:9],data.valid.labels[0:9]})
cls_true = data.valid.cls[0:9]
correct = (cls_true == cls_pred)
correct_sum = correct.sum()
acc = float(correct_sum)
'''''
'''
optimize(num_iterations=1)

print_test_accuracy()

x_guess_batch, y_guess_true = data.validation.next_batch(9)
feed_dict_guess = {x: x_guess_batch,
                   y_true: y_guess_true}
cls_pred_guess = session.run(y_pred_cls,feed_dict=feed_dict_guess)
cls_true = [label.argmax() for label in y_guess_true]

plot_images(images=x_guess_batch,
            cls_pred=cls_pred_guess,
            cls_true=cls_true)
'''


        
