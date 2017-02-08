#!/usr/bin/env python3
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def upsample(img):
        up = np.zeros((2*len(img), 2*len(img[0]), 3), np.float64)
        for i in range(len(img)):
                for j in range(len(img[0])):
                        up[2*i][2*j] = img[i][j]
        return up

def upsampleBlur(greyImg, h):
	if h != "gaus":
		return upsample(cv2.filter2D(greyImg, -1, h, borderType=cv2.BORDER_REFLECT_101))
	else:
		return upsample(cv2.GaussianBlur(greyImg, (7,7), 1))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		a = 0
		if(sys.argv[1][-5:] == '.tiff'):
			a = -5
		else:
			print("ok")
			a = -4
		filts = [np.array([[0, 0, 0],[0,1,0],[0,0,0]]),
		np.array([1,2,1])/4.0,
		np.array([1,4,6,4,1])/16.0,
		"gaus",
		np.array([-0.0000, -0.1196, 0, 0.3131, 0.5000, 0.3131, 0, -0.1196, -0.0000])]
		for i in range(3):
			for filt in range(5):
				p = sys.argv[1][0:a]+'/'+str(i)+str(filt+1)+sys.argv[1][a:]
				print('g'+p)
				greyImg = cv2.imread('g'+p)
				print(str(len(greyImg))+'x'+str(len(greyImg[0]))+'x'+str(len(greyImg[0][0])))
				result = upsampleBlur(greyImg, filts[filt])
				print(str(len(result))+'x'+str(len(result[0]))+'x'+str(len(result[0][0])))
				result = cv2.cvtColor(result.astype('uint8'), cv2.COLOR_BGR2GRAY)
				print(str(len(result))+'x'+str(len(result[0])))
				img = None
				if i == 0:
					g = cv2.cvtColor(cv2.imread(sys.argv[1]), cv2.COLOR_BGR2GRAY) 
					print(str(len(g))+'x'+str(len(g[0]))+'\n')
					img = cv2.subtract(g, result) 
				else:
					print('g'+sys.argv[1][0:a]+'/'+str(i-1)+str(filt+1)+sys.argv[1][a:])
					g = cv2.cvtColor(cv2.imread('g'+sys.argv[1][0:a]+'/'+str(i-1)+str(filt+1)+sys.argv[1][a:]), cv2.COLOR_BGR2GRAY)
					print(str(len(g))+'x'+str(len(g[0]))+'\n')
					img = cv2.subtract(g,result)
				cv2.imwrite('l'+p, img)
	else:
		print("Missing image argument")
	

	
