import cv2 as cv
import numpy as np


# 双线性模糊：边缘保留的噪声模糊
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)


# 均值迁移
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


src = cv.imread("C:\\Users\\ZhouYu\\Desktop\\9.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()