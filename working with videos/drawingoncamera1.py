import cv2
# CALLBACK FUCNTION


def draw_rectangle(event, x, y, flags, param):

    global pt1, pt2, topleft_clicked, bottomright_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if topleft_clicked and bottomright_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topleft_clicked = False
            bottomright_clicked = False
        if topleft_clicked == False:
            pt1 = (x, y)
            topleft_clicked = True
        elif bottomright_clicked == False:
            pt2 = (x, y)
            bottomright_clicked = True

    pass


# GLOBAL VARIABLES
pt1 = (0, 0)
pt2 = (0, 0)
topleft_clicked = False
bottomright_clicked = False

cap = cv2.VideoCapture(0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    ret, frame = cap.read()

    if topleft_clicked:
        cv2.circle(frame, center=pt1, radius=2,
                   color=(0, 0, 255), thickness=-1)

    if topleft_clicked and bottomright_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
