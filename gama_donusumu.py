import numpy as np
import cv2

img = cv2.imread('img/image.jpg')
width=500
height=500
up_points=(width,height)
img = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)


gamma_two_point_three = np.array(255*(img/255)**3,dtype='uint8')

gamma_point_four = np.array(255*(img/255)**4,dtype='uint8')

gamma_point_five = np.array(255*(img/255)**5,dtype='uint8')

img3 = cv2.hconcat([gamma_two_point_three,gamma_point_four,gamma_point_five])
cv2.imshow('a2',img3)
cv2.waitKey(0)
