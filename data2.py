#!/usr/bin/env python

import cv2 as cv
import numpy as np
import video
import math
import os
import time


if __name__ == '__main__':
    cv.namedWindow("result")
    cap = video.create_capture(1)

    path = 'IMG'
    color_red = (0, 0, 128)
    hsv_min = np.array((35, 34, 130), np.uint8)
    hsv_max = np.array((55, 130, 232), np.uint8)

    i = -100
    while True:
        flag, img = cap.read()
        img = cv.flip(img, 1)
        width = np.size(img, 1)
        try:
            cv.putText(img, "%d" % (i), (550, 400), cv.FONT_HERSHEY_SIMPLEX, 1, color_red, 2)
            if i > 0:
                cv.imwrite(os.path.join(path, 'test-{id}.jpg'.format(id=i)), img)
                time.sleep(3)
            i += 1
            cv.imshow('result', img)
        except:
            cap.release()
            raise
        ch = cv.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv.destroyAllWindows()
