#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(data):
    # Initialize the OpenCV bridge
    bridge = CvBridge()

    try:
        # Convert the ROS Image message to an OpenCV image
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")

        # Display the image using OpenCV
        cv2.imshow("Image Viewer", cv_image)
        cv2.waitKey(1)  # Keep the window open

    except Exception as e:
        rospy.logerr("Error processing the image: %s", str(e))

def image_viewer():
    rospy.init_node('image_viewer', anonymous=True)
    rospy.Subscriber('image_topic', Image, image_callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down...")
        cv2.destroyAllWindows()

if __name__ == '__main__':
    image_viewer()
