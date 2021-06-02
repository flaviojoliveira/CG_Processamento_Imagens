import numpy as np
import cv2

img=cv2.imread('milho.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

altura=img.shape[0]
largura=img.shape[1]

for i in np.arange(3, altura-3):
    for j in np.arange(3, altura-3):
        vizinhos=[]
        for k in np.arange(-3,4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                vizinhos.append(a)
    vizinhos.sort()
    median=vizinhos[24]
    b=median
    img_out.itemset((i,j),b)

cv2.imwrite('mediana.jpg', img_out)

cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
