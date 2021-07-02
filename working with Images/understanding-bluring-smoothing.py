import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_img():
    img = cv2.imread(
        '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img)


i = load_img()

gamma = 1/4
i = np.power(i, gamma)

display_img(i)
plt.show()
