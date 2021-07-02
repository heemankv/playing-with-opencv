import cv2
import numpy as np
import matplotlib.pyplot as plt


blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)

cv2.rectangle(blank_img, pt1=(384, 0), pt2=(
    510, 150), color=(0, 255, 0), thickness=10)

cv2.rectangle(blank_img, pt1=(200, 200), pt2=(
    250, 250), color=(0, 255, 0), thickness=7)

cv2.circle(img=blank_img, center=(100, 100),
           radius=50, color=(0, 255, 0), thickness=10)

cv2.circle(img=blank_img, center=(400, 400),
           radius=50, color=(0, 255, 0), thickness=-1)

cv2.line(blank_img, pt1=(0, 0), pt2=(512, 512),
         color=(0, 255, 0), thickness=1)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(blank_img, "hello", (20, 500), font,
            4, (0, 255, 255), 4, lineType=cv2.LINE_AA)


blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)

vertices = np.array([[100, 300], [200, 200], [400, 300],
                    [200, 400]], dtype=np.int32)

pts = vertices.reshape((-1, 1, 2))

cv2.polylines(blank_img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)

plt.imshow(blank_img)
plt.show()
