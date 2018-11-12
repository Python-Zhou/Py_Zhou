import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def mean_demo(m1, m2):
    M1 = cv.mean(m1)
    M2 = cv.mean(m2)
    print(M1)
    print(M2)


def mean_dev_demo(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[0:2]  # 获取数组m1[高，宽，通道数],
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)

def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1, m2)
    dst1 = cv.bitwise_or(m1, m2)
    cv.imshow("logic_demo_and", dst)
    cv.imshow("logic_demo_or", dst1)


src1 = cv.imread("C:\\Users\\ZhouYu\\Desktop\\8.jpg")
src2 = cv.imread("C:\\Users\\ZhouYu\\Desktop\\9.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
cv.imshow("input image1", src1)
cv.imshow("input image2", src2)


# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)
# mean_demo(src1, src2)
# mean_dev_demo(src1, src2)
logic_demo(src2, src1)
cv.waitKey(0)

cv.destroyAllWindows()