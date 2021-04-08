# Avaliação 01 - CGPI

## Critérios de realização e avaliação

- Objetividade e correta grafia de palavras.
- Utilização dos recursos de formatação/marcação do arquivo roteiro.md (Markdown) este arquivo deverá ser duplicado e renomeado para *seuprimeironome_oficial_1.md* dentro do repositório #*CG_Processamento_Imagens/avaliacao_01/seuprimeironome/*#
- inserir os demais arquivos com seus respectivos nomes dentro do diretório citado no item anterior.

Exemplo de estrutura de seu diretório:

```
- seuprimeironome_oficial_1
    - seuprimeironome_oficial_1.md
    - q4_seuprimeironome_oficial_1.ipynb
    - q5_seuprimeironome_oficial_1.ipynb
    - q6_seuprimeironome_oficial_1.ipynb
    - q7_seuprimeironome_oficial_1.ipynb    
    - q8_seuprimeironome_oficial_1.ipynb    
    - q9_seuprimeironome_oficial_1.ipynb    

```
##### *Aqueles que utilizem os editores de código ou IDE em suas máquinas, favor enviar os arquivos no formato .py*

### Atividades

1. Sobre Computação Gráfica e Processamento de Imagens:

    a. Descreva o perfil esperado para um profissional em computação gráfica.
    
    O profissional de computação gráfica deve ter um perfil criativo e tem habilidades em design, edição efeitos sonoros, visuais, criação e animação de objetos 2D e 3D, entre outras habilidades pertinentes.

    b. Onde podemos aplicar ou encontrar aplicação de recursos da computação gráfica.

    Entre as áreas de aplicação da Computação Gráfica podem se apresentar: O CAD/CAm e CAE, que sao sistemas gráficos interativos utilizados para projetar componentes e peças de sistemas mecânicos, elétricos, eletromecânicos e eletrônicos. Em Controle de processos pode ser feito sistemas de controle de tráfego aéreo além de controle de usinas nucleares ou sistemas de produção diversos. Na Cartografia, a computação gráfica é utilizada para produtiz representações precisas e esquemáticas de fenômenos naturais e geográficos obtidos a partir da coleta de dados. E no Entretenimento o desenvolvimento de jogos, que é um dos mercados de maior crescimento e com maior expectativa para os próximos anos.
    
    c. Qual definição de computação gráfica melhor se aplica a um cientista da computação?

    Segundo a ISO ("International Standards Organization") a Computação Gráfica pode ser definida como o conjunto de métodos e técnicas utilizados para converter dados para um dispositivo gráfico, via computador. ela também pode ser entendida como o conjunto de algoritmos, técnicas e metodologias para o tratamento e a representação gráfica de informações através da criação, armazenamento e manipulação de desenhos em formato digital, utilizando-se computadores e periféricos gráficos.

2. Quais diferenças se aplicam ao trabalharmos com imagens vetoriais e matriciais em CGPI (Computação Gráfica e Processamento de Imagens)?

    Uma diferença é que imagens vetoriais não perdem qualidade quando mudamos elas de tamanho enquanto as imagens matriciais perdem qualidade.
    Nas imagens Vetoriais as equações matemáticas descrevem as formas enquanto na matricial essa definição é feita por números binários.


3. Como podemos definir e exemplificar a seguinte imagem abaixo:

   ![Q3_Fig1](/avaliacao_01/data/img1.jpg)

   Na figura Modelagem e Captura de Imagem são formas de salvar uma cena ou imagem do mundo real ou não atravez de cameras, modelagem 3D, desenhos e aplicaticos entre outras formas, trazendo assim formas para o mundo digital.


    ### Sites indicados:

    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

    [<img height="100px" src="https://cdn.freebiesupply.com/logos/thumbs/2x/replit-logo.png">](https://replit.com/)


4. Classifique a imagem gerada por este código (Matricial ou Vetorial) e implemente com novos novos valores (linhas 3 a 12)

   ![Q4_Fig2](/avaliacao_01/data/2img.png)

5. Proponha um exemplo de criação de imagem utilizando a biblioteca Pycairo.
Em seu diretório inserir o arquivo com **APENAS** o código fonte. Nome do arquivo *q5_seuprimeironome.ipynb*

    Consultar:

    https://pycairo.readthedocs.io/en/latest/getting_started.html

    http://www.tortall.net/mu/wiki/CairoTutorial

    https://pypi.org/project/pycairo/

6. Implemente o código abaixo:

    ```
    # Exemplo para uso do Pillow
    # Converte as cores de uma imagem, rotacionando o matiz
    ```

    ```
    from PIL import Image
    from colorsys import rgb_to_hsv, hsv_to_rgb

    im_obj=Image.open('q6.jpg')

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
        shimg.save("q6%02d.jpg"%shift)

    shimg.close()
    im_obj.close()
    ```
    
    E comente o resultado obtido relacionando-o com a utilização da biblioteca Pillow.

    ```
    resposta q6 ...
    ```

#### poste no discord os resultados obtidos (arquivos gerados). Utilizar o canal **#laboratórios**

7. Utilizando a biblioteca Pillow (fork da Pill) e outras (caso necessário) proponha um código fonte que exemplifique a criação de uma Thumbnail.

8. Utilizando a biblioteca Pygames e outras proponha um código fonte que exemplifique a criação de figuras/modelos geométricos.

    - Consultar:
    https://www.pygame.org/wiki/GettingStarted
    https://pypi.org/project/pygame/


9. A partir da imagem **q9_fig.jpg** disponível em *CG_Processamento_Imagens\data\input* elabore um código fonte que realize os seguintes procedimentos:

 - Exibir o formato do arquivo;
 - Exibir o modo do canal formato de pixel 
 - Dimensão da imagem em pixel
 - Exibir as propriedades da imagem em um array de pixel
 - Exibir o array de pixel como imagem
 - converter o array de pixel em objeto Image Pillow
 - verificar o tipo do objeto
 - converter um objeto do tipo imagem para um array numpy
 - Imprimir em tela os atributos do array
 - imprimir (salvar) a imagem no formato PNG
 - imprimir (salvar) a imagem no formato GIF
 - Exibir a imagem e verificar o formato:
 - Converter a imagem em escala de cinza
 - Exibir tamanho
 - Gerar thumbnail ignorando aspecto ratio
 - Flip da imagem (inverter)
 - Exibir coordenadas específicas