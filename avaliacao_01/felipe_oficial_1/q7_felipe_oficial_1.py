from PIL import Image

imagem = Image.open("bandeira_da_franca.png")
MAX_SIZE = (100, 100)

imagem.thumbnail(MAX_SIZE)

imagem.save('bandeira_thumbnail.png')
imagem.show()