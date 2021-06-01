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
    
    Resposta: O perfil é daquele que tem uma visão abrangente para as possibilidades que a computação gráfica tem a disponibilizar e que tenha conhecimento para manipular os programas ou bibliotecas que são próprias para esse recurso.

    b. Onde podemos aplicar ou encontrar aplicação de recursos da computação gráfica.
    
    Resposta: Na criação e edição de imagens digitais; em modelagens de pessoas, ambientes, e objetos em 3D ou 2D para jogos e outras aplicações; design de arquitetura e produtos industriais; modelos de prototipação, entre outros.

    c. Qual definição de computação gráfica melhor se aplica a um cientista da computação?
    
    Resposta: Estudo da manipulação de objetos visuais, virtuais ou não, através de técnicas computacionais.

2. Quais diferenças se aplicam ao trabalharmos com imagens vetoriais e matriciais em CGPI (Computação Gráfica e Processamento de Imagens)?

Resposta: Imagens vetoriais não podem ser exibidas diretamente, pois são cálculos matemáticos que descrevem uma imagem, elas podem ser depois impressas em qualquer tipo de superficie pela sua resolução escalável. Imagens matriciais são as que podemos ver, pois são formados por pixels bidimensionais, porém são limitados quanto à sua resolução.

3. Como podemos definir e exemplificar a seguinte imagem abaixo:

   ![Q3_Fig1](/avaliacao_01/data/img1.jpg)


    Resposta: A imagem digital pode ser obtida por capturas de imagens do mundo físico, utilizando sensores, como uma câmera fotográfica e processada por um programa ou pode ser modelada através de programas (Blender) e bibliotecas específicos para isso (pycairo ou pillow).


4. Classifique a imagem gerada por este código (Matricial ou Vetorial) e implemente com novos novos valores (linhas 3 a 12)

   ![Q4_Fig2](/avaliacao_01/data/2img.png)
   
   Resposta: Se trata de uma imagem vetorial, ou seja, ela possui uma descrição de imagem que pode ser processada.
   

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
    Resposta: O programa imprime a altura e largura da imagem, depois faz um processamento para alterar a matiz das cores utilizando o modelo de cores HSV.
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
