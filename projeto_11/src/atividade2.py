import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
"""
Recebe uma img e retorna amostra aplicando fator n
"""
def amostragem(img, n):
amostra = [lin[::n] for lin in img[::n]]
return np.array(amostra)
 
"""
Testes unitários"""
class AmostragemTests(unittest.TestCase):
 
def test_gera_amostragem_imagem_3por4(self):
m = np.array([[1, 2, 3, 4], [10, 2, 5, 7], [3, 3, 5, 6]])
am = amostragem(m, 2)
np.testing.assert_array_equal(am, [[1, 3], [3, 5]])
 
def test_gera_amostragem_imagem_(self):
m = np.array([[1, 2, 3, 4], [10, 2, 5, 7], [3, 3, 5, 6]])
am = amostragem(m, 3)
self.assertEquals(len(am), 1)
np.testing.assert_array_equal(am, [[1, 4]])
 
if __name__ == "__main__":
unittest.main()
 
# Teste
# abre imagens e cria novas imagens aplicando amostragem
fontes = ['tucano-grayscale.png', 'lion_nature.jpg']
 
fator = 4
for filename in fontes:
img = cv2.imread(filename, 0)
amostra = q.amostragem(img, fator)
 
name, extension = os.path.splitext(filename)
new_filename = '{name}-amostragem-{n}{ext}'.format(name=name, n=fator, ext=extension)
cv2.imwrite(new_filename, amostra)