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


img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text="bricks", org=(10, 600), fontFace=font,
            fontScale=10, color=(255, 0, 0), thickness=4)

kernel = np.ones(shape=(5, 5), dtype=np.float32)/25
print(kernel)

dst = cv2.filter2D(img, -1, kernel)

# display_img(dst)

img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text="bricks", org=(10, 600), fontFace=font,
            fontScale=10, color=(255, 0, 0), thickness=4)

blurred = cv2.blur(img, (10, 10))
# display_img(blurred)


blurred_img = cv2.GaussianBlur(img, (5, 5), 10)

# display_img(blurred_img)


img = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/sammy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

noise_img = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/sammy_noise.jpg')

median_img = cv2.medianBlur(noise_img, 5)

# display_img(median_img)


img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text="bricks", org=(10, 600), fontFace=font,
            fontScale=10, color=(255, 0, 0), thickness=4)

blur = cv2.bilateralFilter(img, 9, 75, 75)
display_img(blur)

plt.show()
