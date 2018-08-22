from socket import *
import cv2
import argparse
import numpy as np
import os


def sendFile(fName):
    host = "192.168.8.111"
    port = 4096
    addr = (host, port)
    buf = 1024
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(fName, addr)
    f = open(fName, "rb")
    data = f.read(buf)
    while data:
        if(s.sendto(data, addr)):
            data = f.read(buf)
    f.close()
    s.close()

def main():

    x = 0

    y = 0

    range_filter = "HSV"

    os.system("ls /dev/ | grep \"video\"")

    videoCapture = raw_input("What video device do you want to use?:")

    camera = cv2.VideoCapture(int(videoCapture))
    camera.set(3, 424)
    camera.set(4, 240)
    ratio = 2#int(FPS)/setFPS
        
    count = 0

    while True:
       ret, image = camera.read()

       if not ret:
           break

       if range_filter == 'RGB':
           frame_to_thresh = image.copy()
       else:
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        thresh = cv2.inRange(frame_to_thresh, (0, 255, 121), (55, 255, 181))

        kernel = np.ones((5,5),np.uint8)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        #cv2.imshow('t',image)
	count = count + 1
	if count == ratio:
                cv2.imwrite("img.jpg", mask)
                sendFile("img.jpg")
                count = 0     

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            print x , "," , y

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break


if __name__ == '__main__':
    cv2.destroyAllWindows()
    cv2.VideoCapture().release()
    main()
