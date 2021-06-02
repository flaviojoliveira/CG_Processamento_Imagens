from numpy import asarray
from matplotlib import pyplot
from matplotlib import image
from PIL import Image

image = Image.open("data/input/q9_fig.jpg")

image
print(image.format)
print(image.mode)
print(image.size)
Image.open("data/input/pixel-rgb.png")

data = image.imread("data/input/q9_fig.jpg")
print(data.dtype)
print(data.shape)
print(data.max())
print(data.min())
pyplot.imshow(data)

image2 = Image.fromarray(data)
type(image2)


image = Image.open("data/input/q9_fig.jpeg")
data = asarray(image)
print(data.dtype)
print(data.shape)
image.save("data/input/q9_fig.png", format="PNG")
image.save("data/input/q9_fig.gif", format="GIF")
image3 = Image.open("data/input/q9_fig.gif")
print(image3.format)

image_gray = image.convert(mode="L")
image_gray
image_gray.save("data/input/q9_fig_gray.jpeg")
image_gray.thumbnail((100, 100))
image_gray

horizontal_image = image2.transpose(Image.FLIP_LEFT_RIGHT)
pyplot.imshow(horizontal_image)
vertical_image = image2.transpose(Image.FLIP_TOP_BOTTOM)
pyplot.imshow(vertical_image)
vertical_image = image2.transpose(Image.ROTATE_270)
pyplot.imshow(vertical_image)

Image.open("data/input/pixel-rgb.png")
