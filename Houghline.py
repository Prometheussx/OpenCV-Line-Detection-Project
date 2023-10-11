# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:10:08 2022

@author: erdem
"""

import cv2
import numpy as np

# Read the image
img = cv2.imread("line.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detection
edges = cv2.Canny(gray, 75, 150)

"""
The cv2.HoughLines() function is computationally intensive.
The first parameter is the image with edges detected.
The second and third parameters are for rho and theta values, which are set to 1 and np.pi/180, respectively.
The fourth parameter is the threshold value, for example, 50.
"""

# Detect lines using the Hough Line Transform with less computational load
# maxLineGap fills in gaps between lines
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=250)

# Extracted line data (x1, y1, x2, y2) for each line
print(lines)

# Iterate through the lines and draw them on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    # Draw lines with specified color (0,255,0) and thickness (2)
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the original image, grayscale image, and edges
cv2.imshow("Image", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
NOTE: The 'lines' data is in the format:
[[[ 46  57 119  57]]
 [[162  62 234  62]]
 [[441 325 608 325]]
 [[442 320 603 320]]
Since each set of lines has only one row, and the starting and ending points of the line are in the 0th element of the set, 
we extract them as x1, y1, x2, y2 using line[0]. 
This allows us to obtain the starting point as (x1, y1) and the ending point as (x2, y2) for each line.
"""
