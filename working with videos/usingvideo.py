import cv2
import time

cap = cv2.VideoCapture('working with videos/firstvideo.avi')
framerate = 2

print(framerate)
if cap.isOpened() == False:
    print("Error file not found or wrong codec!")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        time.sleep(1)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break


cap.release()
cv2.destroyAllWindows()
