#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
  for i in range(0,359):
    print(str(i) + ": " + str(msg.ranges[i]))

rospy.init_node('view_scannums')
sub = rospy.Subscriber('/scan',LaserScan,callback)

rospy.spin()
