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
    ```
    Resposta: 
    ```
    
    b. Onde podemos aplicar ou encontrar aplicação de recursos da computação gráfica.
    ```
    Resposta: 
    ```
    
    c. Qual definição de computação gráfica melhor se aplica a um cientista da computação?
    ```
    Resposta: 
    ```

2. Quais diferenças se aplicam ao trabalharmos com imagens vetoriais e matriciais em CGPI (Computação Gráfica e Processamento de Imagens)?

    ```
    Resposta: 
    ```

3. Como podemos definir e exemplificar a seguinte imagem abaixo:

   ![Q3_Fig1](/avaliacao_01/data/img1.jpg)


    ### Sites indicados:

    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

    [<img height="100px" src="https://cdn.freebiesupply.com/logos/thumbs/2x/replit-logo.png">](https://replit.com/)

    ```
    Resposta: 
    ```
4. Classifique a imagem gerada por este código (Matricial ou Vetorial) e implemente com novos novos valores (linhas 3 a 12)

   ![Q4_Fig2](/avaliacao_01/data/2img.png)

    ```
    Resposta: Vetorial
    ```
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
    Resposta Q6: Os resultados geram novas cores paras imagens utilizando manipulação com conversão de HSV para novos valores e retornando para RGB.
    ```

#### poste no discord os resultados obtidos (arquivos gerados). Utilizar o canal **#laboratórios**

7. Utilizando a biblioteca Pillow (fork da Pill) e outras (caso necessário) proponha um código fonte que exemplifique a criação de uma Thumbnail.

8. Utilizando a biblioteca Pygames e outras proponha um código fonte que exemplifique a criação de figuras/modelos geométricos.

    - Consultar:
    https://www.pygame.org/wiki/GettingStarted
    https://pypi.org/project/pygame/


9. A partir da imagem **q9_fig.jpg** disponível em *CG_Processamento_Imagens\data\input* elabore um código fonte que realize os seguintes procedimentos:

 - [x] Exibir o formato do arquivo;
 - [x] Exibir o modo do canal formato de pixel 
 - [x] Dimensão da imagem em pixel
 - [x] Exibir as propriedades da imagem em um array de pixel
 - [x] Exibir o array de pixel como imagem
 - [x] converter o array de pixel em objeto Image Pillow
 - [x] verificar o tipo do objeto
 - [x] converter um objeto do tipo imagem para um array numpy
 - [x] Imprimir em tela os atributos do array
 - [x] imprimir (salvar) a imagem no formato PNG
 - [x] imprimir (salvar) a imagem no formato GIF
 - [x] Exibir a imagem e verificar o formato:
 - [x] Converter a imagem em escala de cinza
 - [x] Exibir tamanho
 - [x] Gerar thumbnail ignorando aspecto ratio
 - [x] Flip da imagem (inverter)
 - [x] Exibir coordenadas específicas