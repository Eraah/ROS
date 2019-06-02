#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import rospy
from std_msgs.msg import String
import numpy as np
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.vgg16 import preprocess_input

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.python.keras.applications import VGG16
from tensorflow.python.keras.optimizers import Adam

path = 'src/ev3/src/'

def callback(data):
	print(data.data)
	vgg16_net = VGG16(weights='imagenet', include_top=False, input_shape=(350, 350, 3))
	vgg16_net.trainable = False

	model = Sequential()
	model.add(vgg16_net)
	# Добавляем в модель новый классификатор
	model.add(Flatten())
	model.add(Dense(256))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	model.add(Dense(4))
	model.add(Activation('softmax'))

	model.compile(loss='categorical_crossentropy',
				  optimizer=Adam(lr=1e-5),
				  metrics=['accuracy'])
	model.load_weights(path + "mnist_model.h5")

	img = image.load_img(path + 'IMG/'+data.data, target_size=(350, 350))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x) / 255
	preds = model.predict(x)
	classes = ['duck', 'none', 'nut', 'wheel']
	print(classes[np.argmax(preds)])
	pub = rospy.Publisher('class', String, queue_size=2)
	time.sleep(1)
	pub.publish(data.data[4] + ' ' + str(classes[np.argmax(preds)]))

def subscriber():
	rospy.init_node('NN')
	rospy.Subscriber("imgpath", String, callback)
	rospy.spin()

if __name__ == '__main__':
    subscriber()
