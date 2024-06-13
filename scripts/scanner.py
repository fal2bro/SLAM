#!/usr/bin/env pyton3

import rospy
from sensor_msgs.msg import Laserscan



def handlescannercb():

    rospy.init_note('ultrasonic_laser')
    pub = rospy.Publisher('scan',Laserscan,queue_size=10)
    rate = rospy.Rate(1)

    scan = LaserScan()
    scan.header.frame_id = 'us_laser_frame'
    scan.angle_min = -1.57 
    scan.angle_max = 1.57
    scan.angle_increment = 3.14 / sample_num
    sdan.time_increment = 0.003012 * sample_num
    scan.range_min = 0.02 
    scan.range_max = 4
    scan.ranges = 


def main():
    while not rospy.is_shutdown():
        handlescanner()
        rate.sleep()

