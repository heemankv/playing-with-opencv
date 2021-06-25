import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open(
    '/home/malcroft/Documents/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')

print(type(pic))

pic_arr = np.asarray(pic)

print(pic_arr)
print(type(pic_arr))

print(pic_arr.shape)

plt.imshow(pic_arr)


pic_red = pic_arr.copy()
# R G B
print(pic_red)
print("lololol")
pic_red[:, :, 1] = 0
pic_red[:, :, 2] = 0

print(pic_red)
plt.imshow(pic_red)

plt.show()
