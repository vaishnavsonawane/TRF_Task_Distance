import cv2
from imutils import paths
import numpy as np
import imutils

def find_object(image):

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	edged = cv2.Canny(gray, 35, 125)

	cnts = cv2.findContours( edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	cnts = imutils.grab_contours(cnts)

	c = max(cnts, key = cv2.contourArea)

	return cv2.minAreaRect(c)

def distance_to_camera(objWdth, fclLnth, perWdth):
	# calculating distance between camera and object
	return (objWdth * fclLnth) / perWdth

# object pre-defined distance from the camera
objDist = 12

# object pre-defined width
objWdth = 6.5

# reading pre-defined image
image = cv2.imread("images/1.jpeg")
# finding contour in image
marker = find_object(image)
# manipulating focal length through pre-defined data
fclLnth = (marker[1][0] * objDist) / objWdth

lst = []
# accessing images from folder
for i in range(1, 5):
	lst.append(str(i) + '.jpeg')


# iterating through images and manipulating result
for imageName in lst:
	# reading images one after another
	image = cv2.imread('images/' + imageName)
	# getting contour
	marker = find_object(image)
	# finding distance
	distInch = distance_to_camera(objWdth, fclLnth, marker[1][0])

	# drawing a box around the image
	box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
	box = np.int0(box)
	cv2.drawContours(image, [box], -1, (0, 0, 0), 3)
	# displaying output on image
	cv2.putText(image, "%.2f Inch" % (distInch), (80, 50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (255, 255, 255), 3)
	print("Image-", imageName,  ": %.2f Inch" % (distInch))
	# full-screen window
	cv2.namedWindow('image- ' + imageName, cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty('image- ' + imageName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	# displaying image
	cv2.imshow("image- " + imageName, image)
	cv2.waitKey(0)