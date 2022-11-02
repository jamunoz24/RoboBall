#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class BorderLap:
	def __init__(self):
          self.lastclosest = 5
	def callback(self, self.msg):
	  closest = 5
	  closestIndex = 0
	  for i in range(0,359):
	    if self.msg.ranges[i] < closest:
	      closest = self.msg.ranges[i]
	      closestIndex = i
	  print(str(closestIndex) + ": " + str(closest));
	  if self.msg.ranges[0] > 1 and self.msg.ranges[270] > 1:
	    move.linear.x = 0.1
	    move.angular.z = 0.0
	  else:
	    move.linear.x = 0.0
	    move.angular.z = 0.5
	  print(str(self.msg.ranges[90]) + " " + str(self.msg.ranges[180]) + " " + str(self.msg.ranges[270]) + " " +  str(self.msg.ranges[359]))
	  pub.publish(move)


if __name__ == '__main__':
  bl = BorderLap()
  rospy.init_node('lab5')
  sub = rospy.Subscriber('/scan',LaserScan,bl.callback)
  pub = rospy.Publisher('/cmd_vel',Twist)
  move = Twist()
  rospy.spin()

