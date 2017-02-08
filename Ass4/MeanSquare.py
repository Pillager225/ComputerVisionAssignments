#!/usr/bin/env python3
import cv2
import numpy as np
import os
import sys
from os.path import isfile, join

if __name__ == "__main__":
	if len(sys.argv) > 1:
		for f in os.listdir(sys.argv[1]): 
			if isfile(join(sys.argv[1], f)):
				a = 0
				if(f[-5:] == '.tiff'):
					a = -5
				else:
					a = -4
				if not 'hist' in f:
					img = cv2.imread(sys.argv[1]+'/'+f)
					squareSum = 0
					pixels = 0
					for row in img:
						for col in row:
							for pix in col:
								squareSum += pix**2
								pixels += 1
					squareSum = squareSum/pixels
					print(f + ": " + str(squareSum))
	else:
		print("Missing directory argument")
