import cv2 as cv
import numpy as np


def extrace_object_demo():  # 标注测定颜色
    capture = cv.VideoCapture("C:\\Users\\ZhouYu\\Desktop\\1.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([156, 43, 46])
        upper_hsv = np.array([180, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow("video", mask)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_sapce_demo(image):  # 色彩空间转换
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb", Ycrcb)


src = cv.imread("C:\\Users\\ZhouYu\\Desktop\\2.png")  # blue, green, red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# color_sapce_demo(src)
# extrace_object_demo()
b, g, r = cv.split(src)  # 分离通道
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

src[:, :, 2] = 0  # 使得第二通道都为0

src = cv.merge([b, g, r])  # 合并通道

cv.imshow("changed image", src)

cv.waitKey(0)

cv.destroyAllWindows()