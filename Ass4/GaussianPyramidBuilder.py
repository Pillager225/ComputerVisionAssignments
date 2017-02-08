#!/usr/bin/env python3
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def downsample(img):
        down = np.zeros((len(img)/2, len(img[0])/2, 3), np.float64)
        for i in range(len(down)):
                if i%2 == 0:
                        for j in range(len(down[0])):
                                if j%2 == 0:
                                        down[i][j] = img[2*i][2*j]
        return down

def blurDownsample(greyImg, h):
	if h != "gaus":
		return downsample(cv2.filter2D(greyImg, -1, h, borderType=cv2.BORDER_REFLECT_101))
	else:
		return downsample(cv2.GaussianBlur(greyImg, (7,7), 1))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		a = 0
		if(sys.argv[1][-5:] == '.tiff'):
			a = -5
		else:
			print("ok")
			a = -4
		greyImg = cv2.cvtColor(cv2.imread(sys.argv[1]), cv2.COLOR_BGR2GRAY)
		pImages = [[greyImg]*5]*3;
		for i in range(3):
			pImages[i][0]= blurDownsample(pImages[i][0], np.array([[0,0,0],[0,1,0],[0,0,0]]))
			pImages[i][1] = blurDownsample(pImages[i][1], np.array([1,2,1])/4.0)
			pImages[i][2] = blurDownsample(pImages[i][2], np.array([1,4,6,4,1])/16.0)
			pImages[i][3] = blurDownsample(pImages[i][3], "gaus")
			pImages[i][4] = blurDownsample(pImages[i][4], np.array([-0.0000, -0.1196, 0, 0.3131, 0.5000, 0.3131, 0, -0.1196, -0.0000])) # TODO
			cv2.imwrite('g'+sys.argv[1][0:a]+'/'+str(i)+'1'+sys.argv[1][a:], pImages[i][0])
			cv2.imwrite('g'+sys.argv[1][0:a]+'/'+str(i)+'2'+sys.argv[1][a:], pImages[i][1])
			cv2.imwrite('g'+sys.argv[1][0:a]+'/'+str(i)+'3'+sys.argv[1][a:], pImages[i][2])
			cv2.imwrite('g'+sys.argv[1][0:a]+'/'+str(i)+'4'+sys.argv[1][a:], pImages[i][3])
			cv2.imwrite('g'+sys.argv[1][0:a]+'/'+str(i)+'5'+sys.argv[1][a:], pImages[i][4])
	else:
		print("Missing image argument")
	

	
