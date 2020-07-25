import cv2
import numpy as np

imgpath = "cat01.jpg"
img = cv2.imread(imgpath)
# cv2.imshow("img", img)
# cv2.waitKey(0)
t1 = np.array([[0, 0, 1]])
t2 = np.array([[1, 1, 1]]).reshape(-1, 1)
src = np.array([[0, 0], [200, 0], [0, 200]], np.float32)
dst = np.array([[0, 0], [100, 0], [0, 100]], np.float32)
print(src)
src1 = np.concatenate((src, t2), axis=1)
print(src1)
print(dst)
A = cv2.getAffineTransform(src, dst)
print(A)
a = np.concatenate((A, t1), 0)
print(a)
B = cv2.getRotationMatrix2D((40, 50), 30, 0.5)
print(B)
print(img.shape)
h, w = img.shape[:2]
img2 = cv2.warpAffine(img, B, (w, h))

# cv2.namedWindow("img2",0)
# cv2.resizeWindow('img2', 400, 300)
# cv2.imshow("img2", img2)
# cv2.waitKey(0)
cv2.imwrite("img2.png", img2)
