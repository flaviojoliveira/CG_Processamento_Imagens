import cv2

img = cv2.imread('imagem.png', cv2.IMREAD_UNCHANGED)

print("Dimensão Original: ", img.shape)

scale_percent = 20
largura = int(img.shape[1] * scale_percent / 100)
altura = int(img.shape[0] * scale_percent / 100)
dim = (largura, altura)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Dimensão Obtida: ', resized.shape)

cv2.imwrite('escala.png', resized)