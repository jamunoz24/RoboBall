#!/usr/bin/env python

import rospy
import moveit_commander

if __name__ == '__main__':
      rospy.init_node('turtlebot3_clap')
      move_group_gripper = moveit_commander.MoveGroupCommander("gripper")
      for i in range(1,15):
	      gripper_joint_goal = [0.01,0.01]
	      move_group_gripper.go(gripper_joint_goal, wait=True)
	      gripper_joint_goal = [0.0001,0.0001]
	      move_group_gripper.go(gripper_joint_goal, wait=True)



