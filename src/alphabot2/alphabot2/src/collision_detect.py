#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO

#set up GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set variables
detect_left_pin = 16
detect_right_pin = 19
status_left = 0
status_right = 0

#configure pins
GPIO.setup(detect_left_pin, GPIO.IN)
GPIO.setup(detect_right_pin, GPIO.IN)

#apply pull up resistors in software
GPIO.setup(detect_left_pin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(detect_right_pin, GPIO.IN, GPIO.PUD_UP)

def check_coll():
	pub = rospy.Publisher('collision', String, queue_size=10)
	rospy.init_node('alphabot2_collision_detection')
	rate = rospy.Rate(10) #10 hz
	while not rospy.is_shutdown():
		#hello_str = "hello world %s" % rospy.get_time()
		#rospy.loginfo(hello_str)
		status_left = GPIO.input(detect_left_pin)
		status_right = GPIO.input(detect_right_pin)
		if(status_left == 0):
			pub.publish('collision_left')
			print('Collision detected on left side')
		if(status_right == 0):
			pub.publish('collision_right')
			print('Collision detected on right side')

		rate.sleep()

if __name__=='__main__':
	try:
		check_coll();
	except rospy.ROSInterruptException:
		pass

