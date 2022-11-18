import cv2
img = cv2.imread('img/angry_sponge.jpg')
print(img.dtype)
img_neg = 255 - img
cv2.imshow('original',img)
cv2.imshow('negative',img_neg)
cv2.waitKey(0)