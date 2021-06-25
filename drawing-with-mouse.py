import cv2
import numpy as np
import matplotlib.pyplot as plt

count = 0


def draw_circle(event, x, y, flags, param):
    global count

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 80, (0, 255, 0), -1)

        count += 1

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 80, (0, 0, 255), -1)
        count += 1

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 80, (0, 0, 0), -1)
        count += 1


cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_circle)

img = np.zeros((512, 512, 3))

while True:

    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

print(count)
