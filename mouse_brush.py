import cv2
import numpy as np
import math


def nothing(x):
    pass


class Paint(object):
    """
    A painting tool using mouse
    """

    def __init__(self):
        """
        Initial some parameters.
        """
        self.press = False  # true if mouse is pressed
        self.mode = 1  # default mode is drawing lines
        self.ix = 0
        self.iy = 0
        self.paper = np.zeros((540, 990, 3), np.uint8)  # Create a black image
        self.color_pat = np.zeros((256, 256, 3), np.uint8)  # Create a small color pat
        self.draw_color = (0, 0, 0)
        self.draw_thickness = [1, 1]  # Line thickness and shape boarder thickness
        self.fill = 0
        self.key = 0xFF

    def draw_on_paper(self):
        """
        Create a window named Paper and call functions bases on keyboard input
        :return:
        """
        # Create a drawing window
        self.paper[:] = 255
        cv2.namedWindow('Paper')
        cv2.imshow('Paper', self.paper)
        # Selecting draw mode
        while True:
            cv2.imshow('Paper', self.paper)
            self.key = cv2.waitKey(1)
            if self.key == 27 & 0xFF:
                break
            elif self.key == ord('1') & 0xFF:
                self.mode = 1
            elif self.key == ord('2') & 0xFF:
                self.mode = 2
            elif self.key == ord('3') & 0xFF:
                self.mode = 3
            elif self.key == ord('4') & 0xFF:
                self.color_bar()
            if self.fill == 0:
                self.draw_thickness[1] = self.draw_thickness[0]
            elif self.fill == 1:
                self.draw_thickness[1] = -1
            cv2.setMouseCallback('Paper', self.draw_mode)
        self.quit()

    def color_bar(self):
        """
        Create a color bar window to choose color and brush size
        :return:
        """

        cv2.namedWindow('color-bar')

        # Create track bars for color change
        cv2.createTrackbar('R', 'color-bar', 0, 255, nothing)
        cv2.createTrackbar('G', 'color-bar', 0, 255, nothing)
        cv2.createTrackbar('B', 'color-bar', 0, 255, nothing)
        cv2.createTrackbar('Thickness', 'color-bar', 1, 5, nothing)
        cv2.createTrackbar('Fill', 'color-bar', 0, 1, nothing)

        # Set track bars location
        cv2.setTrackbarPos('R', 'color-bar', self.draw_color[2])
        cv2.setTrackbarPos('G', 'color-bar', self.draw_color[1])
        cv2.setTrackbarPos('B', 'color-bar', self.draw_color[0])
        cv2.setTrackbarPos('Thickness', 'color-bar', self.draw_thickness[0])
        cv2.setTrackbarPos('Fill', 'color-bar', self.fill)

        while True:
            cv2.imshow('color-bar', self.color_pat)
            self.key = cv2.waitKey(1)
            if self.key == 27 & 0xFF:
                break
            # get current positions of four track bars
            r = cv2.getTrackbarPos('R', 'color-bar')
            g = cv2.getTrackbarPos('G', 'color-bar')
            b = cv2.getTrackbarPos('B', 'color-bar')
            self.draw_thickness[0] = cv2.getTrackbarPos('Thickness', 'color-bar')
            self.fill = cv2.getTrackbarPos('Fill', 'color-bar')
            self.color_pat[:] = [b, g, r]
            self.draw_color = (b, g, r)
        cv2.destroyWindow('color-bar')

    def draw_mode(self, event, x, y, flags, param):
        """

        :param event: Mouse callback event
        :param x: mouse horizontal position
        :param y: mouse vertical position
        :param flags: None
        :param param: None
        :return:
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.press = True
            self.ix, self.iy = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            distance = int(math.sqrt((x - self.ix) ** 2 + (y - self.iy) ** 2))
            self.press = False
            # Drawing in line mode
            # self.key = cv2.waitKey(1) & 0xFF
            if self.mode == 1:
                cv2.line(self.paper, (self.ix, self.iy), (x, y), self.draw_color, self.draw_thickness[0], cv2.LINE_AA)
            # Drawing in circle mode
            elif self.mode == 2:
                cv2.circle(self.paper, (self.ix, self.iy), distance, self.draw_color, self.draw_thickness[1],
                           cv2.LINE_AA)
            # Drawing in rectangle mode
            elif self.mode == 3:
                cv2.rectangle(self.paper, (self.ix, self.iy), (x, y), self.draw_color, self.draw_thickness[1],
                              cv2.LINE_AA)

    def quit(self):
        """
        Quit window
        :return: whether quit or not
        """
        # Create a quit window
        cv2.namedWindow('Quit')
        quit_img = np.zeros((63, 100, 3), np.uint8)
        quit_img[:] = 255
        # Text message inside window
        font = cv2.FONT_HERSHEY_DUPLEX
        text = 'Quit?'
        text_size = cv2.getTextSize(text, font, 1, 2)[0]
        text_x = int((quit_img.shape[1] - text_size[0]) / 2)
        text_y = int((quit_img.shape[0] + text_size[1]) / 2)
        cv2.putText(quit_img, text, (text_x, text_y), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

        cv2.imshow('Quit', quit_img)
        cv2.createTrackbar('No/Yes', 'Quit', 0, 1, nothing)
        while True:
            decision = cv2.getTrackbarPos('No/Yes', 'Quit')
            self.key = cv2.waitKey(1)
            if decision == 1:
                return cv2.destroyAllWindows()
            elif self.key == 27 & 0xFF:
                break
        cv2.destroyAllWindows()
