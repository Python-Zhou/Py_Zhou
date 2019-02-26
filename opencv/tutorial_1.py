import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)  # 打开摄像机。在括号里面输入路径可以读取视频。
    while(True):
        ret, frame = capture.read()  # 读取摄像头,它能返回两个参数，第一个参数是bool型的ret，其值为True或False，代表有没有读到图片；第二个参数是frame，是当前截取一帧的图片
        frame = cv.flip(frame,1)  # 水平翻转
        cv.imshow("video", frame)
        if cv.waitKey(10) & 0XFF == ord('q'):   # 键盘输入q退出窗口，不按q点击关闭会一直关不掉 也可以设置成其他键
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)   # 尺寸和通道数
    print(image.size)   # 像素数据
    print(image.dtype)   # 每个通道所占的位数
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread("C:\\Users\\ZhouYu\\Desktop\\1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# video_demo()
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 获取灰度图像
cv.imwrite("C:\\Users\\ZhouYu\\Desktop\\result.jpg", gray)
cv.waitKey(0)

cv.destoryALLWindows()


