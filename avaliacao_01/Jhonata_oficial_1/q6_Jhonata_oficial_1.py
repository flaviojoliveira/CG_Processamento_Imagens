from PIL import Image
from colorsys import rgb_to_hsv, hsv_to_rgb

im_obj=Image.open('q6.png')

print ("width = "+str(im_obj.width))
print ("height = "+str(im_obj.height))

shimg=im_obj.copy()
pix=shimg.load()

for shift in range(1,6):
    for i in range(im_obj.width):
        for j in range(im_obj.height):
            rgb=pix[i,j]
            hsv=rgb_to_hsv(*rgb)
            hsv=((hsv[0]+1.0/6)%1.0,hsv[1],hsv[2])
            r,g,b=hsv_to_rgb(*hsv)
            rgb=(int(r),int(g),int(b))
            pix[i,j]=rgb
    shimg.save("q6%02d.png"%shift)

shimg.close()
im_obj.close()