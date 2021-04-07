import cv2

img=cv2.imread('imagem.png',cv2.IMREAD_UNCHANGED)

print("Dimensao Original: " img.shape)

scale_percent=20
largura = int (img.shape[1]* scale_percent/100)
altura = int (img.shape[0]* scale_percent/100)
dim=(largura,altura)

resized= cv2.resized(img, dim, interpolationcv2.INTER_AREA)

print("Dimensao Obtida: ", resized.shape)

cv2.write('escala.png', resized)