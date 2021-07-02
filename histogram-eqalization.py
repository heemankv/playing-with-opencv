import cv2
import numpy as np
import matplotlib.pyplot as plt


rainbow = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

img = rainbow
print(img)

mask = np.zeros(img.shape[:2], np.uint8)

mask[300:400, 100:400] = 255

masked_image = cv2.bitwise_and(img, img, mask=mask)
show_masked = cv2.bitwise_and(show_rainbow, show_rainbow, mask=mask)

hist_mask_values_red = cv2.calcHist(
    [rainbow], channels=[2], mask=mask, histSize=[256], ranges=[0, 256])

hist_mask_values = cv2.calcHist(
    [rainbow], channels=[2], mask=None, histSize=[256], ranges=[0, 256])


plt.imshow(hist_mask_values)
plt.show()
