import cv2 as cv


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


src = cv.imread("C:\\Users\\PythonZhou\\Desktop\\1.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)
cv.destoryALLWindows()
help(cv.namedWindow)
