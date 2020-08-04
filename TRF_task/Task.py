import cv2
from imutils import paths
import numpy as np
import imutils

def find_object(image):

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	gray = cv2.GaussianBlur(gray, (5, 5), 0)

	edged = cv2.Canny(gray, 35, 125)

	cnts = cv2.findContours( edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	cnts = imutils.grab_contours(cnts)

	c = max(cnts, key = cv2.contourArea)

	return cv2.minAreaRect(c)