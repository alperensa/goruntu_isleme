
import cv2

img = cv2.imread('img/image.jpg') # Load image
cv2.imshow("orijinal hali",img)
img_median = cv2.medianBlur(img, 3) # Add median filter to image

cv2.imshow('img', img_median) # Display img with median filter
cv2.waitKey(0)        # Wait for a key press to
cv2.destroyAllWindows # close the img window.