import cv2
import matplotlib.pyplot as plt

img = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)

plt.imshow(img)
plt.show()
