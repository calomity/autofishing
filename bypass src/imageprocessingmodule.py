# this file for convert to avaible read image.

import os, sys
import numpy as np
import cv2
from PIL import Image
import logmodule

# usage:
# imageprocessingmodule.firstconvert('img/deneme.png')
# imageprocessingmodule.secondconvert("img/first.png")
# imageprocessingmodule.lastconvert("img/second.png")

if os.path.exists('img'):
	logmodule.log('"img" Klasoru bulundu. ',1)
else:
	logmodule.log('"img" Klasoru bulunamadi. ',2)

def secondconvert(path):
	img = cv2.imread(path)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h,s,v = cv2.split(hsv)
	th, threshed = cv2.threshold(v, 150, 255, cv2.THRESH_BINARY_INV)
	dst2 = cv2.bitwise_and(img, img, mask=threshed)
	cv2.imwrite("img/second.png", dst2)
	logmodule.log('"img/second.png" yazildi. ',1)
def lastconvert(path):
	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
	cv2.imwrite('img/last.png', thresh)
	logmodule.log('"img/last.png yazildi. ',1)
	#os.remove('img/screen.png')
def firstconvert(path):
	image = cv2.imread(path)
	original = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	lower = np.array([150, 100, 220], dtype="uint8")
	upper = np.array([172,111,255], dtype="uint8")
	mask = cv2.inRange(image, lower, upper)
	cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]
	cv2.fillPoly(mask, cnts, (255,255,255))
	result = cv2.bitwise_and(original,original,mask=mask)
	cv2.imwrite('img/first.png', result)
	logmodule.log('"img/first.png" yazildi. ',1)
firstconvert("img/canyou.png")
