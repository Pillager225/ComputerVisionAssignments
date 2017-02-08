#!/usr/bin/env python3
import cv2
import numpy as np
import os
import sys
from os.path import isfile, join

def getHist(img):
	h = np.zeros((300,256,3))
	
	bins = np.arange(256).reshape(256,1)
	color = [ (255,0,0),(0,255,0),(0,0,255) ]
	
	for ch, col in enumerate(color):
		hist_item = cv2.calcHist([img],[ch],None,[256],[0,255])
		cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
		hist=np.int32(np.around(hist_item))
		pts = np.column_stack((bins,hist))
		cv2.polylines(h,[pts],False,col)

	return np.flipud(h)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		for f in os.listdir(sys.argv[1]): 
			if isfile(join(sys.argv[1], f)):
				a = 0
				if(f[-5:] == '.tiff'):
					a = -5
				else:
					a = -4
				hist = getHist(cv2.imread(sys.argv[1]+'/'+f))
				cv2.imwrite(sys.argv[1]+"/"+f[:a] + "hist.jpg", hist)
			
	else:
		print("Missing image argument")
