from PIL import Image

def japaoband(height):
    WHITE = (255, 255, 255)
    CRIMSON = (188, 0, 45)
    width = 3*height//2
    raio = 3*height//10
    centro = (width//2, height//2)

    image = Image.new("RGB", (width, height), WHITE)
    for x in range(centro[0]-raio, centro[0]+ raio):
        for y in range(centro[1]-raio, centro[1]+ raio):
            if (x-centro[0])**2 + (y-centro[1])**2 <= raio**2:
                image.putpixel((x, y), CRIMSON)

    return image


t = japaoband(700)
t.show()
t.save("japao.png", format="png")