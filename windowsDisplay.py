import cv2
import numpy as np


class Application:
    def display(self, img):
        img = np.array(img)
        # Convert RGB to BGR
        img = img[:, :, ::-1].copy()
        cv2.imshow("Screen sharer", img)
        cv2.waitKey()
