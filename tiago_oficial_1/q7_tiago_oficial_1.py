from PIL import Image

def generateThumbnail(file, size):
   try:
      image = Image.open(file)
      image.thumbnail(size)
      image.save('thumbnail_%s' % file)
      print ('Thumbnail gerado.')

   except Exception as error:
      print (error)

generateThumbnail('imagem.jpg', (128,128))