#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class BorderLap:
	def __init__(self):
	  self.test = 0
	def callback(self, msg):
	  closest = 5
	  closestIndex = 0
	  for i in range(0,359):
	    if msg.ranges[i] < closest:
	      closest = msg.ranges[i]
	      closestIndex = i
	  print(str(closestIndex) + ": " + str(closest));
	  if msg.ranges[0] > 1 and msg.ranges[270] > 1:
	    move.linear.x = 0.1
	    move.angular.z = 0.0
	  else:
	    move.linear.x = 0.0
	    move.angular.z = 0.5
	  print(str(msg.ranges[90]) + " " + str(msg.ranges[180]) + " " + str(msg.ranges[270]) + " " +  str(msg.ranges[359]))
	  pub.publish(move)
	  self.test = self.test + 1
	  print(self.test)

if __name__ == '__main__':
  bl = BorderLap()
  rospy.init_node('lab5')
  sub = rospy.Subscriber('/scan',LaserScan,bl.callback)
  pub = rospy.Publisher('/cmd_vel',Twist)
  move = Twist()
  rospy.spin()

