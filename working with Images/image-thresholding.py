import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/crossword.jpg', 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def show_pic(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


# not a very good way
ret, th1 = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)

# need to get an addaptive thresholding

th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)


# blending the two ways

blended = cv2.addWeighted(th1, 0.6, th2, 0.4, 0)


show_pic(blended)
