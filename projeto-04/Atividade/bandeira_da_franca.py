from PIL import Image, ImageDraw

RED = (255, 0, 0)  # vermelho
WHITE = (255, 255, 255)  # branco
BLUE = (0, 0, 255)  # azul


def criar_bandeira(nome, largura=300, altura=200):  # definição das variáveis da função
    bandeira = Image.new("RGB", (largura, altura))  # definição dos parâmetros da imagem
    x, y = largura // 3, 2 * largura // 3  # coordenadas das colunas
    draw = ImageDraw.Draw(bandeira)  # aplicação da biblioteca Image.Draw para criar a imagem
    draw.rectangle((0, 0, x, altura), RED)  # criação do retângulo vermelho
    draw.rectangle((x, 0, y, altura), WHITE) # criação do retângulo branco
    draw.rectangle((y, 0, largura, altura), BLUE)   # criação do retângulo azul
    bandeira.save(nome) # salvar o arquivo com o nome especificado


criar_bandeira("bandeira_da_franca.png")  # chamada da função com parâmetro do nome do arquivo
