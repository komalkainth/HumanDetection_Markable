from __future__ import print_function
from imutils import paths
import numpy as np
import argparse
from imutils import paths
import cv2
from operator import add
import os
import sys
 
# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--images", required=True, help="Path of the directory that contains all the images for detection")
args = vars(parser.parse_args())

#WFunction for smaller bounding box. 
def draw_boxes (image_name, points):

      newPoint3, newPoint4 = int (point3*0.015), int (point4*0.015)
      cv2.rectangle(image_name,(point1+newPoint3,point2+newPoint4), (point3-newPoint3,point4-newPoint4), (255,0,0), 2)

# initialize the Default person detector of OpenCV
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# loop over the image paths in the folder.
for imagePath in paths.list_images(args["images"]):
    image = cv2.imread(imagePath)
    #image_copy = image.copy()  #Making a copy of image on which smaller bounding boxes are being made. UNCOMMENT FOR SMALLER BOUNDING BOXES
    print ("Image path:", imagePath)
    print ("size of image is:", image.shape)
    rows,cols, dim = image.shape
    #if size is smaller than given value, image is being resized for better bounding box. 
    if rows < 800:
      image = cv2.resize(image,(500,1500))
    # Deetction of human present in a picture  
    (rects, weights) = hog.detectMultiScale(image, winStride=(1, 1),padding=(8, 8), scale=1.05)
    cv2.imshow('Input', image)  
    xArray = []
    yArray = []
    hArray = []
    wArray = []
    #It removes the different bounding boxes and creates only one box
    # if no human is found, just show input as the output 
    if len(rects) == 0:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
    else:
        for (x,y,w,h) in rects:
            xArray.append(x)
            yArray.append(y)
            wArray.append(w)
            hArray.append(h)
        point1 = min (xArray)
        point2 = min (yArray)
        newW = map (add, xArray, wArray)
        newH = map (add, yArray, hArray)
        point3 = max (newW)
        point4 = max (newH)
        points = [point1, point2, point3, point4]
        #drawing the rectangle from maximum, minimum point found
        cv2.rectangle(image,(point1,point2), (point3,point4), (0,0,255), 2)
        #draw_boxes(image_copy,points) #UNCOMMENT FOR SMALLER BOUNDING BOXES
        #resizing the image to fit the screen
        image = cv2.resize(image,(300,600))
        #image_copy = cv2.resize(image_copy,(300,600)) #UNCOMMENT FOR SMALLER BOUNDING BOXES
        cv2.imshow("Image", image)
        #cv2.imshow("Shrunk Bounding Box", image_copy) #UNCOMMENT FOR SMALLER BOUNDING BOXES
        cv2.waitKey(0)



