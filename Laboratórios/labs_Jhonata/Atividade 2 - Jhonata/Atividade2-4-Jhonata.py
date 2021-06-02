import cv2

imagem = cv2.imread('line.png', cv2.IMREAD_UNCHANGED)

print('Dimensão Original: ', imagem.shape)

scale_percent = 20 
largura = int (imagem.shape[1] * scale_percent /100)
altura = int (imagem.shape[0] * scale_percent/100)

dim = (largura, altura)

resized = cv2.resize(imagem, dim, interpolation = cv2.INTER_AREA)

print("Dimensão Obitida", resized.shape)

cv2.imwrite('escala.png', resized)