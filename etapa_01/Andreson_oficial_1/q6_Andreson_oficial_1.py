from PIL import Image
from colorsys import rgb_to_hsv, hsv_to_rgb

image = Image.open("./avaliacao_01/Andreson_oficial_1/q6.jpg")

print ("width = "+str(image.width))
print ("height = "+str(image.height))

shimg=image.copy()
pix=shimg.load()

for shift in range(1,6):
    for i in range(image.width):
        for j in range(image.height):
            rgb=pix[i,j]
            hsv=rgb_to_hsv(*rgb)
            hsv=((hsv[0]+1.0/6)%1.0,hsv[1],hsv[2])
            r,g,b=hsv_to_rgb(*hsv)
            rgb=(int(r),int(g),int(b))
            pix[i,j]=rgb
    shimg.save("q6%02d.jpg"%shift)

shimg.close()
image.close()