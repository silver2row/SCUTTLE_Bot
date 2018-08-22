import cv2
import argparse
import numpy as np
import os

def main():

    x = 0

    y = 0

    range_filter = "HSV"

    os.system("ls /dev/ | grep \"video\"")

    videoCapture = raw_input("What video device do you want to use?:")

    camera = cv2.VideoCapture(int(videoCapture))

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

	print x , "," , y

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break


if __name__ == '__main__':
    main()
