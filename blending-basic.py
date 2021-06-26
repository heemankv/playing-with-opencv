import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# blending images of same size

# resizing images
img1 = cv2.resize(img1, (1200, 1200))
img2 = cv2.resize(img2, (1200, 1200))

# blending
blended = cv2.addWeighted(img1, 0.9, img2, 0.2, 10)


# overlay small image on top of a larger image ( no blending)
img1 = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


img2 = cv2.resize(img2, (300, 300))

x_offset = 0
y_offset = 0

x_end = x_offset + img2.shape[1]
y_end = y_offset + img2.shape[0]
print(img1.shape)
print(img2.shape)

img1[y_offset:y_end, x_offset:x_end] = img2

# blend images of different sizes


plt.imshow(img1)
plt.show()
plt.imshow(img2)
plt.show()
plt.imshow(blended)
plt.show()
