import numpy as np
import cv2

# Creat a background
logo = np.zeros((512, 512, 3), np.uint8)
bgd_color = 173, 111, 26
cv2.rectangle(logo, (0, 0), (512, 512), bgd_color, -1, cv2.LINE_AA)

# Top circle
cv2.ellipse(logo, (256, 128), (64, 64), 90, 30, 330,  (0, 0, 255), -1, cv2.LINE_AA)
cv2.ellipse(logo, (256, 128), (24, 24), 0, 0, 360,  bgd_color, -1, cv2.LINE_AA)

# Left circle
cv2.ellipse(logo, (181, 258), (64, 64), 0, 0, 300,  (0, 255, 0), -1, cv2.LINE_AA)
cv2.ellipse(logo, (181, 258), (24, 24), 0, 0, 360,  bgd_color, -1, cv2.LINE_AA)

# Right circle
cv2.ellipse(logo, (331, 258), (64, 64), 270, 30, 330,  (255, 0, 0), -1, cv2.LINE_AA)
cv2.ellipse(logo, (331, 258), (24, 24), 0, 0, 360,  bgd_color, -1, cv2.LINE_AA)

# logo text
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(logo, 'OpenCV', (105, 400), font, 2.5, (255, 255, 255), 4, cv2.LINE_AA)

# Show the logo design
cv2.imshow('Drawing', logo)
cv2.waitKey(0)
cv2.destroyAllWindows()