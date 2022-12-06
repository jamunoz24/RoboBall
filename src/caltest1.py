#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('user_move', anonymous=True)
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=20)
    vel_msg = Twist()

    #Receiveing the user's input
    choice = input("Move (0) or turn (1)?")
    if choice == 0:
      speed = input("Input your speed:")
      distance = input("Type your distance:")
      vel_msg.linear.x = abs(speed)
      #Since we are moving just in x-axis
      vel_msg.linear.y = 0
      vel_msg.linear.z = 0
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = 0

      #Setting the current time for distance calculus
      t0 = rospy.Time.now().to_sec()
      current_distance = 0

      #Loop to move the turtle in an specified distance
      while(current_distance < distance):
        #Publish the velocity
#        print vel_msg
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        print current_distance
    elif choice == 1:
      direction = input("Left (0) or Right (1)?")
      if direction == 0:
        direction = 1;
      else:
        direction = -1;
      movetime = input("Enter seconds for turn")
      t0 = rospy.Time.now().to_sec()
      t1 = rospy.Time.now().to_sec()
      vel_msg.linear.x = 0
      vel_msg.linear.y = 0
      vel_msg.linear.z = 0
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = 0.06 * direction
      while(movetime > (t1-t0)):
        print(t1-t0)
        print movetime
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        t1=rospy.Time.now().to_sec()
    else:
      print("Invalid entry")
      
    #After the loop, stops the robot
    t0 = rospy.Time.now().to_sec()
    t1 = rospy.Time.now().to_sec()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    while(t1-t0 < 3):
    #Force the robot to stop
      print t1-t0
      print(vel_msg)
      velocity_publisher.publish(vel_msg)
      t1 = rospy.Time.now().to_sec()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
    print("done")
