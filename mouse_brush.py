import cv2
import numpy as np
import math

drawing = True  # true if mouse is pressed
rec_mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


# mouse callback function
def draw(event, x, y, flags, param):
    global ix, iy, drawing, rec_mode, color_set

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        distance = int(math.sqrt((x - ix) ** 2 + (y - iy) ** 2))
        if rec_mode:
            cv2.rectangle(paper, (ix, iy), (x, y), color_set, 6, cv2.LINE_AA)
        else:
            cv2.circle(paper, (ix, iy), distance, color_set, -1, cv2.LINE_AA)


def nothing(x):
    pass


# Create a black image, a window and bind the function to window
size = 512
color_set = (0, 0, 0)
paper = np.zeros((size, size, 3), np.uint8)
paper[:] = 255
color_pat = np.zeros((64, 64, 3), np.uint8)
color_pat[:] = 0
cv2.namedWindow('image')
cv2.namedWindow('color-bar')

# create track bars for color change
cv2.createTrackbar('R', 'color-bar', 0, 255, nothing)
cv2.createTrackbar('G', 'color-bar', 0, 255, nothing)
cv2.createTrackbar('B', 'color-bar', 0, 255, nothing)

while True:
    cv2.imshow('image', paper)
    cv2.imshow('color-bar', color_pat)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        rec_mode = not rec_mode
    elif k == ord('c'):
        paper[:] = 255
    elif k == 27:
        break

    # get current positions of four track bars
    r = cv2.getTrackbarPos('R', 'color-bar')
    g = cv2.getTrackbarPos('G', 'color-bar')
    b = cv2.getTrackbarPos('B', 'color-bar')
    # s = cv2.getTrackbarPos(switch, 'color-bar')

    color_set = [b, g, r]
    color_pat[:] = [b, g, r]
    cv2.setMouseCallback('image', draw)

cv2.destroyAllWindows()
