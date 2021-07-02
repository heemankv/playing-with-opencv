import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import gradient


def load_img():
    blank_img = np.zeros((600, 600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img, text='ABCDE', org=(50, 300),
                fontFace=font, fontScale=5, color=(255, 255, 255), thickness=30)
    return blank_img


def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


img = load_img()

kernal = np.ones((5, 5), dtype=np.uint8)
eroded_img = cv2.erode(img, kernal, iterations=4)


img = load_img()

white_noise = np.random.randint(low=0, high=2, size=(600, 600))

white_noise = white_noise * 255

noise_img = white_noise + img


opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernal)


img = load_img()

black_noise = np.random.randint(low=0, high=2, size=(600, 600))
black_noise = black_noise * -255

black_noise_img = img + black_noise

black_noise_img[black_noise_img == -255] = 0

closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernal)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)


display_img(gradient)
