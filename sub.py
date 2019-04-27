#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


def callback(data):
	print(data.data)
	pub = rospy.Publisher('class', String, queue_size=10)
	pub.publish(data.data)
	# rospy.loginfo("%s", data.data)

def subscriber():
	rospy.init_node('imgpath_topic_subscriber')
	rospy.Subscriber("imgpath", String, callback)
	rospy.spin()


if __name__ == '__main__':
    subscriber()





