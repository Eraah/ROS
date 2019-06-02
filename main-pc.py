#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

items = []
i = 0

# НАЧИНАЕМ НУМЕРАЦИЮ КАРТИНОК С ЕДИНИЦЫ

def printMessage(items, empty):
	step = 1
	for j in range(4):
		if items[j][2:] == 'none':
			continue
		print(str(step) + ' - take ' + items[j][2:] + 'on position' + items[j][0] + 'and put it on 0 position')
		step += 1
		for k in empty:
			print(str(step) + ' - take ' + items[j][2:] + 'on position' + items[j][0] + 'and put it on empty position' + k[0])
			step += 1

def callback(data):
	global i
	items.append(data.data)

	empty = []
	if i == 3:
		while 1:

			step = 1
			print('Текущие объекты ' + str(items))
			print('Какой объект вы хотите перенести:')

			for j in range(4):
				if items[j][2:] == 'none':
					empty.append(items[j][0])
					continue
				else:
					print(str(j+1) + ' - ' + items[j][2:])

			user_obj = input('Ваш выбор: ')

			step = 1

			print('Куда перенести объект: ' )
			for k in (empty):
				print(str(step) + ' - свободная позиция ' + k)
				step += 1
			print(str(step) + ' - положить на нулевую позицию')

			user_act = input('Ваш выбор: ')

			for k in items:
				if (int(k[0]) == int(user_obj)):
					# items[int(user_obj) - 1] = str(user_obj) + ' none'
					break
			else:
				items[int(user_obj) - 1] = str(user_obj) + ' none'
	i += 1


def subscriber():
	rospy.init_node('mainpc')
	rospy.Subscriber("class", String, callback)
	rospy.spin()


if __name__ == '__main__':
    subscriber()