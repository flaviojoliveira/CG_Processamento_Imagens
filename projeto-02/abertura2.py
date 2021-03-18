from PIL import Image
#from utils import in_file
import os

# abrindo nossa imagem
image = Image.open(r"data/input/bandeira.jpeg")

px = image.load() 
cordinate = x, y = 512, 375

# using getpixel method 
#print(image.getpixel(90,60))
print (image.getpixel(cordinate)); 

# exibir a imagem
image.show()