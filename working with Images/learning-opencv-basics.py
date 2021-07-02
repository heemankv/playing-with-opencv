import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')

print(type(img))

print(img.shape)

matplotlib_fix = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_gray = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
print(img_gray)
# plt.imshow(img_gray, cmap='gray')
new_img = cv2.resize(matplotlib_fix, (1000, 400))
w_ratio = 0.5
h_ratio = 0.5

new_img = cv2.resize(matplotlib_fix, (0, 0), matplotlib_fix, w_ratio, h_ratio)


new_img2 = cv2.flip(matplotlib_fix, 1)

cv2.imwrite('new_pic.jpg', new_img2)


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.imshow(new_img2)

# plt.imshow(new_img2)


plt.show()
