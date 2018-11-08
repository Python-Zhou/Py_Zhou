import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print("width : {0}, height : {1}, channel : {2}".format(height, width, channel))
    for row in range(height):  # 遍历图像的每个像素点
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixel_date", image)

# 像素去反,inverse是自带的API，速度快
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("取反", dst)


def creat_image():
    '''
    三通道
    img = np.zeros([400, 400, 3], np.uint8)  #  创建数组
    img[:, :, 1] = np.ones([400, 400])*255
    img[:, :, 2] = np.ones([400, 400]) * 255
    cv.imshow("自制图片", img)

    img = np.ones([400, 400], np.uint8)
    img = img * 0
    cv.imshow("自制图片", img)
    cv.imwrite("C:\\Users\\ZhouYu\\Desktop\\black.png", img)
    '''

    m1 = np.ones([3, 3], np.uint8)  # float32是浮点数，uint8是整数，int32
    # m1.fill(122.388)
    print(m1)

    m2 = m1.reshape([1, 9])  # 二维转一维
    print(m2)

    m3 = np.array([[2, 1, 2], [3, 1, 5], [4, 5, 1]], np.int32)  # 数值任意赋予
    m3.fill(9)
    print(m3)

src = cv.imread("C:\\Users\\ZhouYu\\Desktop\\1.jpg")  # blue, green, red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
# inverse(src)
# access_pixels(src)
creat_image()
t2 = cv.getTickCount()
print("time: {0} s".format((t2-t1)/cv.getTickFrequency()))  # 计算运算时间
cv.waitKey(0)

cv.destroyAllWindows()