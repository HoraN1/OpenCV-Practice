import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal line
# cv2.line(img_name, (start point), (end point), (color), thickness)
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw a rectangle
# cv2.rectangle(img_name, (start point), (end point), (color), thickness)
# thickness -1 for fill
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Draw a circle
# cv2.circle(img_name, (center point), radius, (color), thickness)
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Draw a ellipse
# cv2.ellipse(img_name, (center point), (length, height), rotation, start angle, end angle, (color), thickness)
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Draw a polygon
# cv2.polylines(img_name, [pts], True, (color))
# Third argument: True will be sealed
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

# Fonts
# cv2.putText(img_name, "text", (start), font, size, (color), thickness, anti_alis)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
