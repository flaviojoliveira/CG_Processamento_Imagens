import cv2
import numpy as np

imagem = cv2.imread('line.png')
num_linhas, num_colunas =imagem.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((num_colunas/2, num_linhas/2), 180, 1)

img_rotation = cv2.warpAffine(imagem, rotation_matrix, (num_colunas, num_linhas))

cv2.imwrite('rotacao.png', img_rotation)
cv2.waitKey()