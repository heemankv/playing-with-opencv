import cv2
import numpy as np
import matplotlib.pyplot as plt

dark_horse = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/horse.jpg')
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)

rainbow = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

bricks = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/bricks.jpg')
show_bricks = cv2.cvtColor(bricks, cv2.COLOR_BGR2RGB)

hist_values_bricks = cv2.calcHist(
    [bricks], channels=[1], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_values_bricks)


img = dark_horse
color = ('b', 'g', 'r')

for i, color in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.title('dark houese')
# plt.imshow(show_horse)
plt.show()
