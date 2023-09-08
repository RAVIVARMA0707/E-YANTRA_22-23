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
# Author List:		[ Ravivarma E D,Sutharsan K,Shithaarthan M,Vijay Anand M ]
# Filename:			navStack.py
# Functions:		
# 					[ Comma separated list of functions in this file ]
# Nodes:		    Add your publishing and subscribing node


####################### IMPORT MODULES #######################
import sys
import traceback
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
##############################################################

################# ADD GLOBAL VARIABLES HERE #################



##############################################################

################# ADD UTILITY FUNCTIONS HERE #################



##############################################################

class move():
    def __init__(self):
            rospy.init_node('ebot_controller', anonymous = True)
            self.pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
            sub = rospy.Subscriber('/ebot/laser/scan',LaserScan,self.laser_callback)
            self.regions = {'bright': 0.0, 'fright': 0.0, 'front': 0.0, 'fleft': 0.0, 'bleft': 0.0} 
    def laser_callback(self,msg):
        global regions
        self.regions = {
            'bright':min(min(msg.ranges[0:1]), 8),
            'front':min(min(msg.ranges[359:365]), 8),
            'front1':min(min(msg.ranges[335:365]), 8),
            'bleft':min(min(msg.ranges[710:719]), 8),
        }
        
    def control_loop(self):
            velocity_msg = Twist()
            rate = rospy.Rate(150) 
            rate1 = rospy.Rate(20)
            velocity_msg = Twist()
            velocity_msg.linear.x = 0
            velocity_msg.linear.y = 0
            velocity_msg.linear.z = 0
            velocity_msg.angular.x = 0
            velocity_msg.angular.y = 0
            velocity_msg.angular.z = 0

            self.pub.publish(velocity_msg)
            rospy.loginfo(self.regions["front"])
            a = 0.65
            b = 8
            e = 0.9
            cond1 = True
            cond2 = False
            cond3 = False
            cond4 = False
            cond5 = False
            cond6 = False
            cond7 = False
            cond8 = False
            cond9 = False
            cond10 =False
            while not rospy.is_shutdown():
                    velocity_msg = Twist()
                    rate1.sleep()
                    while cond1 == True:
                        if self.regions["front"] >= 8:
                            velocity_msg.linear.x = 0.2
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= 6 and self.regions["front"] < 8 :
                            velocity_msg.linear.x = 0.7
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= a and self.regions["front"] < 6 :
                            velocity_msg.linear.x = 1.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                            if self.regions["front"] <= a:
                                velocity_msg.linear.x = 0.0
                                velocity_msg.angular.z = 0.0
                                self.pub.publish(velocity_msg)
                                cond1 = False
                                cond2 = True
                                break
                    while cond2 ==True:
                        if self.regions["bleft"]!=b:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 1.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["bleft"] ==b:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0    
                            self.pub.publish(velocity_msg)                                   
                            cond2 = False 
                            cond3 = True
                            break
                    while cond3 ==True:
                        if self.regions["front"] >= 1.9 :
                            velocity_msg.linear.x = 0.5
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] <= 1.9:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                            cond3 = False
                            cond4 = True
                            break
                    while cond4 ==True:
                        velocity_msg.linear.x = 0.0
                        velocity_msg.angular.z = 1.0
                        self.pub.publish(velocity_msg)
                        if self.regions["front"] ==b and self.regions["bright"] <=2.2:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0     
                            self.pub.publish(velocity_msg)                                  
                            cond2 = False 
                            cond5 = True
                            break
                    while cond5 ==True:
                        if self.regions["front"] >= 7.5:
                            velocity_msg.linear.x = 0.5
                            velocity_msg.angular.z = 0.06
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] <=7.5:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                            cond5 = False
                            cond6 = True
                            break
                    while cond6 ==True:
                        if self.regions["front"] >= 7:
                            velocity_msg.linear.x = 0.55
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= 6 and self.regions["front"] < 7 :
                            velocity_msg.linear.x = 0.65
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= 4 and self.regions["front"] < 6 :
                            velocity_msg.linear.x = 0.8
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= e and self.regions["front"] < 4 :
                            velocity_msg.linear.x = 1.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] <=e:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                            cond5 = False
                            cond7 = True
                            break
                    while cond7 ==True:
                        if self.regions["bleft"]!=b:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 1.0
                            self.pub.publish(velocity_msg)
                        if self.regions["bleft"] ==b:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0    
                            self.pub.publish(velocity_msg)                                   
                            cond7 = False 
                            cond8 = True
                            break
                    while cond8 ==True:
                        if self.regions["front"] >= 2.27:
                            velocity_msg.linear.x = 0.5
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] <=2.27:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                            cond8 = False
                            cond9 = True
                            break
                    while cond9 ==True:
                            if self.regions["front1"]!=8:
                                velocity_msg.linear.x = 0.0
                                velocity_msg.angular.z = 0.5
                                self.pub.publish(velocity_msg)
                            elif self.regions["front1"] ==8  :
                                velocity_msg.linear.x = 0.0
                                velocity_msg.angular.z = 0.0    
                                self.pub.publish(velocity_msg)                                   
                                cond9 = False 
                                cond10 = True
                                break
                    while cond10 ==True:
                        if self.regions["front"] >= 7.0:
                            velocity_msg.linear.x = 0.5
                            velocity_msg.angular.z = 0.04
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] <=7.0:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                            cond10 = False
                            cond11 = True
                            break
                    while cond11 ==True:
                        if self.regions["front"] >= 6:
                            velocity_msg.linear.x = 0.6
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= 5 and self.regions["front"] < 6 :
                            velocity_msg.linear.x = 0.8
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= 4 and self.regions["front"] < 5 :
                            velocity_msg.linear.x = 1.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] >= 3 and self.regions["front"] < 4 :
                            velocity_msg.linear.x = 1.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                        elif self.regions["front"] <=3:
                            velocity_msg.linear.x = 0.0
                            velocity_msg.angular.z = 0.0
                            self.pub.publish(velocity_msg)
                            cond11 = False
                            cond12 = True
                            break
                    rate.sleep()
                    velocity_msg.linear.x = 0.0
                    velocity_msg.angular.z = 0.0
                    self.pub.publish(velocity_msg)
                    break 

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS PART #########    
if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Python Script Started!!          ")
        print("------------------------------------------")
        x =move()   
        x.control_loop()
        
    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Python Script Executed Successfully   ")
        print("------------------------------------------")