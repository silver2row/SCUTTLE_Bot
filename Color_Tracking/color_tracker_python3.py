import cv2
import argparse
import numpy as np
import os
#import socket


#IP = "localhost"	# Beagle Bone AP Default Gateway IP
#PORT = 1221		# Beagle Bone Color Tracker Port

camera_number = 0   # Can be listed with "ls /dev/video*"

x = 0
y = 0

range_filter = "HSV"

camera = cv2.VideoCapture(camera_number)

while True:

   ret, image = camera.read()

   if not ret:
       break

   if range_filter == 'RGB':
       frame_to_thresh = image.copy()
   else:
    frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    thresh = cv2.inRange(frame_to_thresh, (15, 147, 148), (64, 255, 255))

    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

#    print(x , "," , y)

#    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    clientSock.sendto(bytes(x), (IP, PORT))
