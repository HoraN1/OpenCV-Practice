import cv2
import numpy as np
import math

drawing = False  # true if mouse is pressed
rec_mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, rec_mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # elif event == cv2.EVENT_MOUSEMOVE:
    #     if drawing:
    #         if rec_mode:
    #             pass
    #         else:
    #             cv2.line(img, (ix, iy), (x, y), (232, 184, 139), 1, cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        distance = int(math.sqrt((x - ix)**2 + (y - iy)**2))
        if rec_mode:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 205, 250), 6, cv2.LINE_AA)
        else:
            cv2.circle(img, (ix, iy), distance, (232, 184, 139), -1, cv2.LINE_AA)


# Create a black image, a window and bind the function to window
size = 512
img = np.zeros((size, size, 3), np.uint8)
img = cv2.rectangle(img, (0, 0), (size - 1, size - 1), (255, 255, 255), -1, cv2.LINE_AA)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        rec_mode = not rec_mode
    elif k == ord('c'):
        img = cv2.rectangle(img, (0, 0), (size - 1, size - 1), (255, 255, 255), -1, cv2.LINE_AA)
    elif k == 27:
        break
cv2.destroyAllWindows()
