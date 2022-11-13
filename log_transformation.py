import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('img/image.jpg')
cv2.imshow("original photo",image)
c = 40
log_image = c * (np.log(image + 1))
log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow(f"Photo After Log Transformation with c={c}",log_image)


c = 30
log_image = c * (np.log(image + 1))
log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow(f"Photo After Log Transformation with c={c}",log_image)

print(log_image)

cv2.waitKey(0)