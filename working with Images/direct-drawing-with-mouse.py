import cv2
import numpy as np
import matplotlib.pyplot as plt

drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, params):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


img = np.zeros((512, 512, 3))
cv2.namedWindow(winname='direct')


cv2.setMouseCallback('direct', draw_rectangle)


while True:

    cv2.imshow('direct', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
