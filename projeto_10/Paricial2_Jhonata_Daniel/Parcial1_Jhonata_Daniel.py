from PIL import Image, ImageFilter

pizza = Image.open("assets/pizza.jpeg")
fritas = Image.open("assets/fritas.jpeg")
hambuguer = Image.open("assets/hambuguer.jpeg")
combo = Image.open("assets/combo.jpeg")

image_blur = pizza.filter(ImageFilter.BLUR)
image_blur.save("assets/pizzablur.jpeg")

image_contour = fritas.filter(ImageFilter.CONTOUR)
image_contour.save("assets/fritascontour.jpeg")

image_details = hambuguer.filter(ImageFilter.DETAIL)
image_details.save("assets/hambuguerdetails.jpeg")

image_smooth = combo.filter(ImageFilter.SMOOTH)
image_smooth.save("assets/combosmooth.jpeg")

image_sharpen = pizza.filter(ImageFilter.SHARPEN)
image_sharpen.save("assets/pizzasharpen.jpeg")

image_emboss = combo.filter(ImageFilter.EMBOSS)
image_emboss.save("assets/comboemboss.jpeg")