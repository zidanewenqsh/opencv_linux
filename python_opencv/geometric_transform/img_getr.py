import cv2
import os
import torch
from tool.utils import makedir
import sys
import numpy as np

filepath = os.path.dirname(__file__)
codepath = os.path.dirname(filepath)
# img size 1024*2048
imgdir1 = os.path.join(codepath, "images")

imgsavedir1 = os.path.join(codepath, "saves")


class ImgAffine:
    def __init__(self, imgdir, imgsavedir, scale=1.0):
        self.imgdir = imgdir

        self.imgsavedir = imgsavedir

        self.num = 0
        self.x1, self.x2, self.x3, self.x4 = 0, 0, 0, 0
        self.y1, self.y2, self.y3, self.y4 = 0, 0, 0, 0
        self.scale = scale
        self.n = 0
        # self.coorddict = {0:(self.x1,self.y1),1:(self.x2,self.y2),2:(self.x3,self.y4),3:(self.x4,self.y4),}

    def get_dist(self, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2).astype(np.int64)

    def draw_rectangle(self, event, x, y, flags, param):

        # ratio = 1 / self.scale
        # self.img2 = self.img
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"self.n: {self.n}")
            if 0 == self.n:
                self.point1 = x, y
                self.x1, self.y1 = self.point1
            if 1 == self.n:
                self.point2 = x, y
                self.x2, self.y2 = self.point2
            if 2 == self.n:
                self.point3 = x, y
                self.x3, self.y3 = self.point3
            if 3 == self.n:
                self.point4 = x, y
                self.x4, self.y4 = self.point4
            # if 4 == self.n:
            #     self.n += 1
            if 4 > self.n:
                print("x1,y1", self.x1, self.y1)
                print(f"point{self.n} {x} {y}")
            if 4 <= self.n:
                self.n = 0
            self.n += 1
            # if 4 < self.n:
            #     self.n = 0

        elif event == cv2.EVENT_RBUTTONDOWN:

            print(f"n {self.n}")
            if 2 == self.n:
                self.n = 0
                d = self.img2
                # d = self.img2.copy()
                cv2.rectangle(d, self.point1, self.point2, (0, 255, 0), 1)
                cv2.imshow("d", d)
                cv2.waitKey(0)
                # cv2.destroyWindow("d")

            if 3 == self.n:
                self.n = 0
                # d = self.img3
                h = self.get_dist(self.point1, self.point2)
                w = self.get_dist(self.point1, self.point3)
                print('wh', w, h, self.w, self.h)
                # print("wh", self.w, self.h)
                src = np.array([self.point1, self.point2, self.point3], np.float32)
                dst = np.array([[0, 0], [0, h], [w, 0]], np.float32)
                # print(src)
                # print(dst)
                # A = cv2.getRotationMatrix2D((self.w/2.0, self.h/2.0), 30, 1)
                A = cv2.getAffineTransform(src, dst)
                # print("A", A)
                # exit()
                d = cv2.warpAffine(self.img3, A, (w, h))

                cv2.imshow("d", d)
                cv2.waitKey(0)
                # cv2.destroyWindow("d")

            if 4 == self.n:
                self.n = 0
                w = self.w
                h = self.h
                src = np.array([self.point1, self.point2, self.point3, self.point4], np.float32)
                dst = np.array([[0, 0], [0, h], [w, h], [w, 0]], np.float32)

                A = cv2.getPerspectiveTransform(src, dst)
                d = cv2.warpPerspective(self.img4, A, (w, h))
                cv2.imshow("d", d)
                cv2.waitKey(0)
            # self.n = 0

    def crop_data(self):

        imgname = "cat01.jpg"
        self.imgpath = os.path.join(self.imgdir, imgname)
        self.imgsavepath = os.path.join(self.imgsavedir, imgname)
        img = cv2.imread(self.imgpath, 1)  # 加载图片
        self.img2 = img.copy()
        self.img3 = img.copy()
        self.img4 = img.copy()
        # height, width = self.img2.shape
        # self.scale = 512/width
        self.img2 = cv2.resize(self.img2, (0, 0), fx=self.scale, fy=self.scale)
        # print(self.img2.shape)
        self.h, self.w = self.img2.shape[:2]
        # cv2.namedWindow("image")
        img = np.zeros((512, 512, 3), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback("image", self.draw_rectangle)
        while (1):
            cv2.imshow("image", self.img2)
            if cv2.waitKey(20) & 0xFF == 27:
                continue
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


if __name__ == '__main__':
    print(0)
    ngdc = ImgAffine(imgdir1, imgsavedir1, scale=1.0)
    ngdc.crop_data()
    # ngdc.save_img()
    # ngdc.dictcheck(imgsavedir=imgsavedir2)
