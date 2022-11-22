#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    global regions_
    translated = []
    for i in range(0,359):
      translated.append(msg.ranges[i])
      if(translated[i] == 0):
        translated[i] = 10;
    regions_ = {
#        'right':  min(min(msg.ranges[210:270]), 10),
#        'fright': min(min(msg.ranges[271:330]), 10),
#        'front':  min(min(msg.ranges[331:359]),min(msg.ranges[0:30]), 10),
#        'fleft':  min(min(msg.ranges[31:90]), 10),
#        'left':   min(min(msg.ranges[91:150]), 10),

#        'right':  min(min(translated[210:270]), 10),
#        'fright': min(min(translated[271:330]), 10),
#        'front':  min(min(translated[331:359]),min(translated[0:30]), 10),
#        'fleft':  min(min(translated[31:90]), 10),
#        'left':   min(min(translated[91:150]), 10),

#        'left':  min(min(translated[210:270]), 10),
#        'fleft': min(min(translated[271:350]), 10),
#        'front':  min(min(translated[331:359]),min(translated[0:30]), 10),
#        'front':  min(min(translated[351:359]),min(translated[0:10]), 10),
#        'fright':  min(min(translated[11:90]), 10),
#        'right':   min(min(translated[91:150]), 10),

        'right':  min(min(translated[271:306]), 10),
        'fright': min(min(translated[307:342]), 10),
        'front':  min(min(translated[343:359]),min(translated[0:18]), 10),
        'fleft':  min(min(translated[19:54]), 10),
        'left':   min(min(translated[55:90]), 10),


    }
    print regions_
    for i in range(0,len(translated)):
      print str(i) + " " + str(translated[i])

rospy.init_node('view_scannums')
sub = rospy.Subscriber('/scan',LaserScan,callback)



rospy.spin()
