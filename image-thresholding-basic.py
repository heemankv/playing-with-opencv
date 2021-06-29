import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/rainbow.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

print(ret)
plt.imshow(thresh1, cmap='gray')
plt.show()
