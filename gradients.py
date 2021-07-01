import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import gradient


# def load_img():
#     blank_img = np.zeros((600, 600))
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(blank_img, text='ABCDE', org=(50, 300),
#                 fontFace=font, fontScale=5, color=(255, 255, 255), thickness=30)
#     return blank_img


def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


img = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/sudoku.jpg', 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

blended = cv2.addWeighted(sobelx, 1, sobely, 1, 0)

ret, th1 = cv2.threshold(blended, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((4, 4), np.uint8)

gradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)

display_img(gradient)


# display_img(th1)
# display_img(sobely)
