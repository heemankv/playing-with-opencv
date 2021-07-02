import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


img2 = cv2.resize(img2, (400, 400))

print(img1.shape)

x_offset = img1.shape[1] - img2.shape[1]
y_offset = img1.shape[0] - img2.shape[0]

print(y_offset, x_offset)
rows, cols, channels = img2.shape

roi = img1[y_offset:img1.shape[0], x_offset:img1.shape[1]]


img2grey = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

mask_inv = cv2.bitwise_not(img2grey)

white_background = np.full(img2.shape, 255, dtype=np.uint8)

bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)

fg = cv2.bitwise_or(img2, img2, mask=mask_inv)

final_roi = cv2.bitwise_or(roi, fg)


large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0],
          x_offset:x_offset+small_img.shape[1]] = small_img

plt.imshow(large_img)
plt.show()
