from PIL import Image

def bandeira_brasil(height):
    GREEN = (0, 156, 59)
    YELLOW = (255, 223, 0)
    BLUE = (0, 39, 118)
    width = 10 * height // 7
    margem = 17 * height // 140
    center = (width // 2, height // 2)
    radius = height // 4

    imagem = Image.new('RGB', (width, height), GREEN)

    # pintando o losango
    for x in range(margem, width - margem):
        for y in range(margem, height - margem):
            if x <= center[0] and y <= center[1] and (center[1] - y) <= 0.64 * (x - margem):
                imagem.putpixel((x, y), YELLOW)
            if x > center[0] and y <= center[1] and (center[1] - y) <= -0.64 * (x - center[0]) + center[1] - margem:
                imagem.putpixel((x, y), YELLOW)
            if x <= center[0] and y > center[1] and (y - center[1]) <= 0.64 * (x - margem):
                imagem.putpixel((x, y), YELLOW)
            if x > center[0] and y > center[1] and (y - center[1]) <= -0.64 * (x - center[0]) + center[1] - margem:
                imagem.putpixel((x, y), YELLOW)

    # pintando o circulo
    for x in range(center[0] - radius, center[0] + radius):
        for y in range(center[1] - radius, center[1] + radius):
            if (x - center[0]) ** 2 + (y - center[1]) ** 2 <= radius ** 2:
                imagem.putpixel((x, y), BLUE)
    return imagem

if __name__ == "__main__":
    bandeira = bandeira_brasil(700)
    bandeira.show()
