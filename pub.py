#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


pub = rospy.Publisher('class', String, queue_size=10)
rospy.init_node('class_topic_publisher')


while not rospy.is_shutdown():
	s = str(raw_input('Enter smth:  '))
	pub.publish(s)

