#!/usr/bin/env python
import rospy
from math import sqrt
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry


class OdometryModifier:

  def __init__(self):
    self.sub = rospy.Subscriber("odom", Odometry, self.callback)
    self.pub = rospy.Publisher('odom2', Odometry, queue_size=10)
    self.total_distance = 0.
    self.previous_x = 0
    self.previous_y = 0
    self.first_run = True

  def callback(self, data):
    if(self.first_run):
      self.previous_x = data.pose.pose.position.x
      self.previous_y = data.pose.pose.position.y
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    d_increment = sqrt((x - self.previous_x) * (x - self.previous_x) +
                   (y - self.previous_y) * (y - self.previous_y))
    self.total_distance = self.total_distance + d_increment
    print str(self.total_distance)
    self.pub.publish(data)
    self.previous_x = data.pose.pose.position.x
    self.previous_y = data.pose.pose.position.y
    self.first_run = False


if __name__ == '__main__':
    rospy.init_node('move_turtlebot', anonymous=True)
    odom = OdometryModifier()
    rospy.spin()
