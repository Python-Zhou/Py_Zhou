import cv2 as cv
import numpy as np


# 均值模糊
def blur_demo(image):
    dst = cv.blur(image, (3, 3))
    cv.imshow("blur_demo", dst)


# 中值模糊
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)


def custom_blur_demo(image):
    # 平滑滤波
    kernel1 = np.ones([5, 5], np.float32)/25  # 25这个数字是为了不让溢出，总体原则就是n=数组每个数值相加之和
    dst = cv.filter2D(image, -1, kernel=kernel1)
    cv.imshow("custom_blur_demo1", dst)

    # 锐化
    kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel2)
    cv.imshow("custom_blur_demo2", dst)


src = cv.imread("C:\\Users\\ZhouYu\\Desktop\\9.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# blur_demo(src)
# median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()