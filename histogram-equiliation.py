import cv2
import numpy as np
import matplotlib.pyplot as plt

gorilla = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/gorilla.jpg', 0)


def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


hist_values = cv2.calcHist([gorilla], channels=[0],
                           mask=None, histSize=[256], ranges=[0, 256])


eq_gorilla = cv2.equalizeHist(gorilla)

eq_hist_values = cv2.calcHist([eq_gorilla], channels=[0],
                              mask=None, histSize=[256], ranges=[0, 256])


color_gorilla = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/gorilla.jpg')
show_gorilla = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2RGB)

hsv_gorilla = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2HSV)

hsv_gorilla[:, :, 2] = cv2.equalizeHist(hsv_gorilla[:, :, 2])
eq_color_gorilla = cv2.cvtColor(hsv_gorilla, cv2.COLOR_HSV2RGB)

# h s v


display_img(eq_color_gorilla)


# plt.plot(hist_values)
# plt.plot(eq_hist_values)
# display_img(eq_gorilla)
# display_img(gorilla)
