import cv2
import matplotlib.pyplot as plt

im = cv2.imread('django.jpg')
print("height",im.shape[0])
print("width",im.shape[1])
im = cv2.resize(im,(500, 500))
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histrn = cv2.calcHist([im],[i],None,[256],[0,256])
    plt.plot(histr,color=col)

cv2.imshow("normal image",im)
cv2.imshow("bw image",bw)
cv2.waitkey(0)