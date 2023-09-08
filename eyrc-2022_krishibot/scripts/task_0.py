#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		Krishi Bot (KB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of Krishi Bot (KB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_0.py
# Functions:		
# 					[ Comma separated list of functions in this file ]
# Nodes:		    Add your publishing and subscribing node


####################### IMPORT MODULES #######################
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys
import traceback
##############################################################

################# ADD GLOBAL VARIABLES HERE #################



##############################################################

################# ADD UTILITY FUNCTIONS HERE #################



##############################################################
class turtlesim:
    def __init__(self):
        rospy.init_node('turtlebot_control', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/turtle1/pose', Pose, self.poseCallback)
        self.pose = Pose()
    def poseCallback(self, data):
        self.pose.theta = round(data.theta,2)
        self.pose.y = round(data.y,2)
    def move(self):
        vel_msg = Twist()
        
        vel_msg.linear.x = 1
        vel_msg.angular.z = abs(1)
        self.pub.publish(vel_msg)
        rate = rospy.Rate(100)
        
        while not rospy.is_shutdown():
            self.pub.publish(vel_msg)
            rate.sleep()
            if self.pose.theta ==3.14:
                vel_msg.linear.x = 0
                vel_msg.angular.z = 0.5
                self.pub.publish(vel_msg)
            if self.pose.theta == -1.57:
                vel_msg.angular.z = 0.0
                self.pub.publish(vel_msg)
                vel_msg.linear.x = 0.5
                self.pub.publish(vel_msg)
            if self.pose.y == 5.5:
                vel_msg.linear.x =0
                self.pub.publish(vel_msg)
                break
        rate.sleep()


######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS PART #########    
if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Python Script Started!!          ")
        print("------------------------------------------")
        x = turtlesim()
        x.move()
        
    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Python Script Executed Successfully   ")
        print("------------------------------------------")
