


#! /usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		Krishi Bot (KB) Theme (eYRC 2022-23)
*        		===============================================
*(rows,cols,channels) = cv_image.shape
  28     if cols > 60 and rows > 60 :
  29       cv2.circle(cv_image, (50,50), 10, 255)
*  This script is to implement Task 2.2 of Krishi Bot (KB) Theme (eYRC 2022-23).
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
# Filename:			percepStack.py
# Functions:		
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
import cv2 
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image,CompressedImage
from std_msgs.msg import String
import numpy as np
import sys
import tf
from threading import Thread
from maniStack import*
import geometry_msgs.msg
# from listner import*

# You can add more if required
##############################################################


# Initialize Global variables


################# ADD UTILITY FUNCTIONS HERE #################

##############################################################

bridge=CvBridge()
global x,y,z,len1,depth_val,lst

def img_clbck(img_msg):
    '''
    Callback Function for RGB image topic

    Purpose:
    -----
    Convert the image in a cv2 format and then pass it 
    to image_processing function by saving to the 
    'image' variable.

    Input Args:
    -----
    img_msg: Callback message.
    '''
    global pub_rgb,image,pose,len1,x,y
    
    
    try:
        # np_arr = np.frombuffer(img_msg.data, np.uint8)    # img_msg is the callback data
        # image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR) # cv_image is the cv2 format image
        image = bridge.imgmsg_to_cv2(img_msg, "bgr8")
        # cv2.imshow("jghiut",image)
        # cv2.waitKey(0)
    except CvBridgeError as e:
        print(e)
    # x=image.shape[1]
    # y=image.shape[0]
    
    pose = image_processing(image)
    # print("pose",pose)
    len1=len(pose)
    
    # pub_rgb.publish(str(pose))
    # rospy.loginfo("jhggfuydgf")
    # pub_rgb.publish(str("hi"))
    
    

def image_processing(image):
    '''
    NOTE: Do not modify the function name and return value.
          Only do the changes in the specified portion for this
          function.
          Use cv2.imshow() for debugging but make sure to REMOVE it before submitting.
    
    1. Find the centroid of the bell pepper(s).
    2. Add the x and y values of the centroid to a list.  
    3. Then append this list to the pose variable.
    3. If multiple fruits are found then append to pose variable multiple times.

    Input Args:
    ------
    image: Converted image in cv2 format.

    Example:
    ----
    pose = [[x1, y1] , [x2, y2] ...... ]
    '''
    
    pose = []
    hsv =cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    low=np.array([90,143,88])
    high=np.array([180,255,255])

    low1=np.array([11,130,76])
    high1=np.array([20,255,255])

    mask=cv2.inRange(hsv,low,high)
    mask1=cv2.inRange(hsv,low1,high1)
    maskt=mask+mask1

    # cv2.imshow("iguy",image)
    # cv2.waitKey(0)
    
    def center(mask1):
        pose=[]
        
        ret,thresh = cv2.threshold(mask1,127,255,0)


        masked_img = cv2.cvtColor(mask1, cv2.COLOR_GRAY2BGR)  
        contours, hierarchy = cv2.findContours(mask1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        all=[]
        m=0
        for i in contours:
            a=cv2.contourArea(i)
            all.append(a)
            if a>550:
                m=m+1
            
        # print(all)  
        
        s=sorted(contours,key=cv2.contourArea,reverse=True)
        
        
        if m>0:
            for i in range(0,m):
                
                    # cv2.drawContours(image,s[i], -1, (60, 200, 200), 3)
                    
                    M = cv2.moments(s[i])
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    # cv2.circle(image, (cX, cY), 5, (255, 255, 255), -1)
                    # cv2.putText(image, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                
                    pose.append([cX,cY])
                    
        return pose
    
    pose=center(maskt)
    # print(pose)
   
    cv2.imshow("sdg",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    # print(pose)   
    return pose

def depth_clbck(depth_msg):
    global depth_val
    
    '''
    Callback Function for Depth image topic

    Purpose:
	--- 
    1. Find the depth value of the centroid pixel returned by the
    image_processing() function.
    2. Publish the depth value to the topic '/center_depth'


    NOTE: the shape of depth and rgb image is different. 
    
    Input Args:
    -----
    depth_msg: Callback message.
    '''
    # x=image.shape[1]
    # y=image.shape[0]
    depth_val = []
    try:
        cv_image = bridge.imgmsg_to_cv2(depth_msg,depth_msg.encoding)    
    except CvBridgeError as e:
        print(e)
    
    # resized_down = cv2.resize(cv_image,(x,y), interpolation= cv2.INTER_LINEAR)
    
    # cv2.imshow("gygy",image)
    # cv2.waitKey(0)
    # print(pose)
    for i in range(0,len1):
        de=cv_image[pose[i][1],pose[i][0]]   
        depth_val.append(de)
    # print(depth_val)
    # print(cv_image[326,58])
    def distance():
        global x
        global y
        global z
        s=[]
        cx=320.5
        cy=240.5
        fx=554.3827128226441
        fy=554.3827128226441
        a=0
        b=0
        for i in range(0,len1):
            x = depth_val[i] * ((pose[i][0]-cx)/fx)
            y = depth_val[i] * ((pose[i][1]-cy)/fy)
            z = depth_val[i]
            # print("haiiiiiiii")
            
            # pixel=image[pose[i][0],pose[i][1]]
            # print(pixel)
            # if pixel[2] > 100 and pixel[1] <= 50 and pixel[0] <= 50:
            #     a=1
            #     print("red")
            # else:
            #     b=1
            #     # print("yel")

            if i==1 :
                br = tf.TransformBroadcaster()
                br.sendTransform((z,-x,-y),tf.transformations.quaternion_from_euler(0,0,0),rospy.Time.now(),'fruit_red','camera_link2')
            elif i==1 :
                br1 = tf.TransformBroadcaster()
                br1.sendTransform((z,-x,-y),tf.transformations.quaternion_from_euler(0,0,0),rospy.Time.now(),'fruit_yellow','camera_link2')
    distance()
    # pub_depth.publish(str(depth_val))



def main2():

    global pub_rgb,pub_depth
    
    sub_image_color_1 = rospy.Subscriber("/camera/color/image_raw2",Image, img_clbck)
    sub_image_depth_1 = rospy.Subscriber("/camera/depth/image_raw2",Image, depth_clbck)

def main():
    rospy.init_node("percepStack", anonymous=True)
    # ur5 = Ur5Moveit()
    # ur5.go_to_predefined_pose("pose7")
    # # i = 0
    while not rospy.is_shutdown():
        main2()
        # i = i+1

    # del ur5
if __name__ == '__main__':
    main()
