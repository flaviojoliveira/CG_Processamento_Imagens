from PIL import Image


def tnails():
    try:
        image = Image.open('C:/Users/Talis/Documents/GitHub/CG_Processamento_Imagens/avaliacao_01/data/epictetus.jpg')
        image.thumbnail((90, 90))
        image.save('C:/Users/Talis/Documents/GitHub/CG_Processamento_Imagens/avaliacao_01/data/thumbnail.jpg')
        image1 = Image.open('C:/Users/Talis/Documents/GitHub/CG_Processamento_Imagens/avaliacao_01/data/thumbnail.jpg')
        image1.show()
    except IOError:
        pass


tnails()
