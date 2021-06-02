# Ray Casting Python Labirinto 3D

Baseado na técnica de Ray Casting, onde os objetos são desenhados inteiramente de linhas verticais. O tamanho e a posição das linhas são definidos pela distância entre o jogador e o objeto. Este é um jogo de labirinto 3D muito simples feito do zero em python, usando apenas três bibliotecas:

* [Numpy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Keyboard](https://pypi.org/project/keyboard/)


Video tutorial aqui: https://youtu.be/5xyeWBxmqzc

## Basicamente

Começaremos com um mapa bem simples, depois faremos um gerador de mapas aleatórios. O mapa é definido por uma matriz, onde uns representam paredes e zeros representam corredores ou espaços vazios. Também precisamos definir uma posição inicial e direção para o jogador, bem como as coordenadas de saída:

<details>
  <summary>Mapa e Inicialização:</summary>
 
```python
import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapa = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]

posx, posy, rot = 1.5, 1.5, np.pi/4
exitx, exity = 3, 3
```
</details>

Agora podemos iniciar o ciclo de visão, com um campo de visão horizontal de 60 °, avançando um grau por iteração. O primeiro raio começará a 30 ° à direita do jogador e o último estará a 30 ° à esquerda. Um raio sempre começa na posição do jogador, com incrementos baseados no seno e cosseno do ângulo do raio em um loop infinito. Um contador é usado para manter o valor da distância que o raio percorreu, caso contrário, pode-se simplesmente usar o teorema de Pitágoras para calcular a distância no final.

Para testar se um raio atingiu uma parede, só temos que verificar as partes inteiras das coordenadas do raio em relação ao mapa. Se houver uma batida, calculamos a altura e saímos do loop while. depois disso, desenhamos uma linha vertical na posição i indo de -h para h.

<details>
  <summary>Looping de Visão:</summary>
 
```python
for i in range(60):
    rot_i = rot + np.deg2rad(i-30)
    x, y = posx, posy
    sin, cos = 0.02*np.sin(rot_i), 0.02*np.cos(rot_i)
    n = 0
    
    while 1:
        x, y, n = x + cos, y + sin, n +1
        if mapa[int(x)][int(y)]:
            h = 1/(0.02*n)
            break
        
    plt.vlines(i, -h, h)

plt.show()
```
</details>

Depois disso, você poderá ver o bloco do meio cercado por paredes! Este é o conceito básico dos gráficos de ray casting, agora podemos transformá-lo em algo que se assemelha a um jogo. Para isso, criamos um loop de jogo que engloba o loop de visão e também funcionará indefinidamente até que o jogo termine. Podemos fazer alguns ajustes na lógica de plotagem: 

* linhas mais grossas `plt.vlines(i, -h, h, lw = 8)`
* ocultar eixo `plt.axis('off')`
* remova os espaços em branco `plt.tight_layout()`
* limite da região do gráfico  `plt.axis([0, 60, -1, 1])`
* substituir `plt.show()`  por `plt.draw()`
* pausar e limpar para o próximo quadro `plt.pause(0.0001); plt.clf()`
* feche a janela quando o jogo acabar `plt.close()`

Para a entrada do usuário, usaremos a biblioteca 'keyboard'. Basicamente, usando as setas do teclado, tentamos mover o jogador para um novo local, mas isso só acontece se o novo local não for uma parede. Se o jogador alcançou a saída ou pressionou a tecla "esc", saímos do loop principal do jogo. Este código deve estar dentro do loop principal do jogo.

<details>
  <summary>Keyboard inputs and game over:</summary>
 
```python
    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == 'up':
        x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
    elif key == 'down':
        x, y = (x - 0.3*np.cos(rot), y - 0.3*np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi/8
    elif key == 'right':
        rot = rot + np.pi/8
    elif key == 'esc':
        break

    if mapa[int(x)][int(y)] == 0:
        if int(posx) == exitx and int(posy) == exity:
            break
        posx, posy = (x, y)
```
</details>



<details>
  <summary>Complete code so far:</summary>
  
  ```python
import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapa = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]

posx, posy, rot = 1.5, 1.5, np.pi/4
exitx, exity = 3, 3

while 1:
    for i in range(60):
        rot_i = rot + np.deg2rad(i-30)
        x, y = posx, posy
        sin, cos = 0.02*np.sin(rot_i), 0.02*np.cos(rot_i)
        n = 0
        
        while 1:
            x, y, n = x + cos, y + sin, n +1
            if mapa[int(x)][int(y)]:
                h = 1/(0.02*n)
                break
            
        plt.vlines(i, -h, h, lw=8)

    plt.axis('off'); plt.tight_layout(); plt.axis([0, 60, -1, 1])
    plt.draw(); plt.pause(0.0001); plt.clf()
    
    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == 'up':
        x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
    elif key == 'down':
        x, y = (x - 0.3*np.cos(rot), y - 0.3*np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi/8
    elif key == 'right':
        rot = rot + np.pi/8
    elif key == 'esc':
        break

    if mapa[int(x)][int(y)] == 0:
        if int(posx) == exitx and int(posy) == exity:
            break
        posx, posy = (x, y)

plt.close()
```
  
</details>

Não é um jogo divertido, mas é um jogo. Vamos fazer algumas melhorias.

## Melhorias
Em primeiro lugar, podemos adicionar um pouco de cor ao jogo. Após a criação do mapa, podemos percorrer todas as suas posições e substituir aquelas com cores RGB aleatórias ou, alternativamente, criar uma matriz secundária para armazenar as cores. Essas cores são recuperadas mais tarde toda vez que batemos em uma parede e usadas para definir o parâmetro "cores" na função vlines. Também adicionaremos um fator de sombreamento com base na distância que o raio percorreu, de forma que paredes mais próximas sejam mais brilhantes.

Também podemos adicionar uma cor para o céu / teto e para o chão, isso pode ser tão simples quanto linhas horizontais grossas desenhadas antes das linhas verticais. O último cosmético que quero discutir são os ladrilhos: da mesma forma que calculamos as alturas quando batemos em uma parede, podemos fazer sempre que a parte inteira de uma das coordenadas muda, posteriormente esses pontos são plotados com a função de gráfico de dispersão (se não aparecer, podemos tornar o piso transparente ou definir o parâmetro zorder para 2 ou algum valor superior). Estes também têm a função de sinalizar a saída para o jogador com uma cor diferente para essas peças.

<details>
  <summary>Código com ajustes cosméticos:</summary>
  
```python
import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapa = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]

for i in range(len(mapa)):
    for j in range(len(mapa)):
        if mapa[i][j] == 1:
            mapa[i][j] = list(np.random.uniform(0,1,3))
            
posx, posy, rot = 1.5, 1.5, np.pi/4
exitx, exity = 3, 3

while 1:
    
    plt.hlines(-0.6, 0, 60, colors='gray', lw=165, alpha=0.5)
    plt.hlines(0.6, 0, 60, colors='lightblue', lw=165)
    tilex, tiley, tilec = [], [], []
    for i in range(60):
        rot_i = rot + np.deg2rad(i-30)
        x, y = posx, posy
        sin, cos = 0.02*np.sin(rot_i), 0.02*np.cos(rot_i)
        n = 0
        
        while 1:
            xx, yy = (x, y)
            x, y, n = x + cos, y + sin, n +1

            # tiles logic
            if abs(int(3*xx)-int(3*x)) > 0 or abs(int(3*yy)-int(3*y))>0:
                tilex.append(i)
                tiley.append(-1/(0.02 * n))
                if int(x) == exitx and int(y) == exity:
                    tilec.append('b')
                else:
                    tilec.append('k')

            if mapa[int(x)][int(y)]:
                h = np.clip(1/(0.02 * n), 0, 1)
                c = np.asarray(mapa[int(x)][int(y)])*(0.3 + 0.7 * h)
                break
            
        plt.vlines(i, -h, h, lw=8, colors=c)
        
    plt.scatter(tilex, tiley, c=tilec, zorder=2) # draw tiles on the floor
    plt.axis('off'); plt.tight_layout(); plt.axis([0, 60, -1, 1])
    plt.draw(); plt.pause(0.0001); plt.clf()
    
    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == 'up':
        x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
    elif key == 'down':
        x, y = (x - 0.3*np.cos(rot), y - 0.3*np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi/8
    elif key == 'right':
        rot = rot + np.pi/8
    elif key == 'esc':
        break

    if mapa[int(x)][int(y)] == 0:
        if int(posx) == exitx and int(posy) == exity:
            break
        posx, posy = (x, y)

plt.close()
```

</details>

Agora tudo que você precisa são alguns labirintos reais para jogar, você pode fazer isso manualmente ou usar algum tipo de gerador de labirinto.

## Gerador de labirinto
O gerador de labirinto que criei é muito simples:
1. Gere uma matriz aleatória com uns e zeros
2. Feche as paredes ao redor do mapa
3. Faça um andador aleatório que comece de um lado do mapa e vá para o outro lado, removendo alguns blocos no caminho.
4. Este caminhante aleatório deve ter preferência por caminhos existentes, apenas removendo blocos quando emperrados.
5. Quando atinge o outro lado, a posição é marcada como a saída

<details>
  <summary>Gerador de labirintos:</summary>
  
```python
#random map generator
size = 15
mapa = [[list(np.random.uniform(0, 1, 3))] * size for i in range(size)]
for i in range(size-2):
    for j in range(size-2):
        if np.random.uniform() > 0.33:
            mapa[i+1][j+1] = 0

posx, posy = (1, np.random.randint(1, size -1))
rot = np.pi/4
x, y = (posx, posy)
mapa[x][y] = 0
count = 0 
while True:
    testx, testy = (x, y)
    if np.random.uniform() > 0.5:
        testx = testx + np.random.choice([-1, 1])
    else:
        testy = testy + np.random.choice([-1, 1])
    if testx > 0 and testx < size -1 and testy > 0 and testy < size -1:
        if mapa[testx][testy] == 0 or count > 5:
            count = 0
            x, y = (testx, testy)
            mapa[x][y] = 0
            if x == size-2:
                exitx, exity = (x, y)
                break
        else:
            count = count+1
```

</details>

# Ray casting 2.0 - com reflexos, melhor sombreamento, paredes de meia altura

Ray casting 2.0 video: https://youtu.be/WhmTa1NGLSE

Vamos começar com o fundo, que antes era apenas duas linhas horizontais, agora vamos usar gradientes para perspectiva adicionada. Os gradientes são plotados usando uma matriz com um espaço linear (np.linspace) e seu brilho muda dependendo do ângulo que o jogador está olhando, invertido para piso e teto. Eu também mudo os ladrilhos por um padrão xadrez, apenas mudando a regra de quando registrar os pontos do ladrilho

<details>
  <summary>Background:</summary>
  
```python
bg = np.linspace(0, 1, 150) #background gradient

...

plt.scatter([30]*150, -bg, c=-bg, s=200000, marker='_', cmap='Greys') #floor
plt.scatter([30]*150, bg, c=bg, s=200000, marker='_', cmap='Blues') #background

...
if int(x*2)%2 == int(y*2)%2: # then record tilex, tiley, tilec

```

</details>

Eu não posso fazer sombras como o jogo de rastreamento de raios, mas posso sombrear de forma diferente cada lado dos blocos de acordo com a "luz" do skybox. Para isso, preciso saber em que lado do bloco um raio cruzou, o que é feito simplesmente por sondagem. Agora temos um mapa de altura que será discutido logo a seguir.

<details>
  <summary>Sombreamento:</summary>
  
```python
    h = np.clip(1/(0.04 * n*np.cos(np.deg2rad(i-30))), 0, 1)
    c = np.asarray(mapc[int(x)][int(y)])*(0.4 + 0.6 * h)
    if maph[int(x+cos)][int(y-sin)] > 0.5:
        c = 0.85*c
        if maph[int(x-cos)][int(y+sin)] != 0 and sin >0:
            c = 0.7*c
```

</details>

Quando o raio atinge um bloco com meia altura, ele armazena sua localização e cor e então continua até atingir um bloco com altura total. Depois disso, desenhamos a linha vertical para o bloco inteiro, que está mais longe, e então desenhamos a parte inferior do meio bloco sobre ele.

<details>
  <summary>Blocos de meia altura:</summary>
  
```python
def caster(x, y, i, ex, ey, maph, mapc, sin, cos, n, half, tx, ty, tc):
    while True: # ray loop
        xx, yy = (x, y)
        x, y = (x + cos, y + sin)
        n = n+1
        if half == None and int(x*2)%2 == int(y*2)%2:#(abs(int(3*xx)-int(3*x)) > 0 or abs(int(3*yy)-int(3*y))>0):
            tx.append(i)
            ty.append(-1/(0.04 * n*np.cos(np.deg2rad(i - 30))))
            if int(x) == ex and int(y) == ey:
                tc.append('b')
            else:
                tc.append('k')
        if maph[int(x)][int(y)] == 1 or (maph[int(x)][int(y)] == 0.5 and half == None):
            h , c = shader(n, maph, mapc, sin, cos, x, y, i)
            if maph[int(x)][int(y)] == 0.5 and half == None:
                half = [h, c, n]
            else:
                break

    return(c, h, x, y, n, half, tx, ty, tc)
```

</details>

As reflexões são feitas de uma forma muito simples, quando um raio atinge um bloco reflexivo, dependendo do lado em que o raio atingiu nós inverteremos uma das direções do raio, se ele atingir uma parede horizontal invertemos a direção vertical do raio e o oposto de uma parede vertical. Para dar uma aparência reflexiva à linha vertical, nós a desenhamos com transparência para que o fundo brilhe e então desenhamos a parede refletida. As coisas ficam mais complicadas quando consideramos as combinações com blocos de meia altura.

<details>
  <summary>Reflexões:</summary>
  
```python
def reflection(x, y, i, ex, ey, maph, mapc, sin, cos, n, c, h, half, tx, ty, tc):
    if half != None:
        plt.vlines(i, 0, h, lw = 8, colors = c, alpha=0.5) #top reflected
        plt.vlines(i, -half[0], 0, lw = 8, colors = half[1])# bottom regular
    else:
        plt.vlines(i, -h, h, lw = 8, colors = c, alpha=0.5) # draw vertical lines
    if maph[int(x+cos)][int(y-sin)] != 0:
        cos = -cos
    else:
        sin = -sin
    c2, h, x, y, n, half2, tx, ty, tc = caster(x, y, i, ex, ey, maph, mapc, sin, cos, n, half, tx, ty, tc)
    c = (c + c2)/2
    if half != None:
        plt.vlines(i, 0, h, lw = 8, colors = c) # draw vertical lines
    else:
        plt.vlines(i, -h, h, lw = 8, colors = c) # draw vertical lines
        if half2 !=  None:
            plt.vlines(i, -half2[0], 0, lw = 8, colors = half2[1])        
    return c, h, x, y, n, half2, tx, ty, tc 
```

</details>


Isso é tudo, as coisas começaram a ficar pesadas para o matplotlib, então também portei tudo para o pygame (junto com o jogo de rastreamento de raios, veja os arquivos). De qualquer forma, aqui está o código para matplotlib:

<details>
  <summary>Código completo com matplotlib:</summary>
  
```python
import numpy as np
from matplotlib import pyplot as plt
from pynput import keyboard, mouse
from time import time

def main():
    size = 15
    global key; key = None # register keypresses
    listener = keyboard.Listener(on_press=on_press);listener.start()
    last_mouse = [0,0]
    posx, posy, rot = (1, np.random.randint(1, size -1), 1) # player pos
    bg = np.linspace(0, 1, 150) #background gradient
    mapc, maph, mapr, ex, ey = maze_generator(posx, posy, size)# map, exit
    plt.figure(num = 'Pycaster 2.0')
    while True: #main game loop
        start = time()
        rot, last_mouse = rotation(rot, last_mouse)
        plt.scatter([30]*150, -bg, c=-bg, s=200000, marker='_', cmap='Greys')
        plt.scatter([30]*150, bg, c=bg, s=200000, marker='_', cmap='Blues')
        tx, ty, tc = ([], [], [])
        for i in range(60): #vision loop
            rot_i = rot + np.deg2rad(i - 30)
            x, y = (posx, posy)
            sin, cos = (0.04*np.sin(rot_i), 0.04*np.cos(rot_i))
            n, half = 0, None
            c, h, x, y, n, half, tx, ty, tc = caster(x, y, i, ex, ey, maph, mapc, sin, cos, n, half, tx, ty, tc)
            
            if mapr[int(x)][int(y)] == 1:
                c, h, x, y, n, half2, tx, ty, tc = reflection(x, y, i, ex, ey, maph, mapc, sin, cos, n, c, h, half, tx, ty, tc)

            else:
                plt.vlines(i, -h, h, lw = 8, colors = c)
                if half !=  None:
                    plt.vlines(i, -half[0], 0, lw = 8, colors = half[1])
            

            
        plt.axis('off'); plt.tight_layout(); plt.axis([0, 60, -1, 1])
        plt.scatter(tx, ty, c=tc, zorder = 2, alpha=0.5, marker='s') # draw ts on the floor
        plt.text(57, 0.9, str(round(1/(time()-start),1)), c='y')
        plt.draw();plt.pause(0.1); plt.clf()
        # player's movement
        posx, posy, rot, keyout = movement(posx, posy, rot, maph)
        if (int(posx) == ex and int(posy) == ey) or keyout == 'esc':
            break

    plt.close()

def maze_generator(x, y, size):
    mapc = np.random.uniform(0,1, (size,size,3)) 
    mapr = np.random.choice([0, 0, 0, 0, 1], (size,size))
    maph = np.random.choice([0, 0, 0, 0, .5, 1], (size,size))
    maph[0,:], maph[size-1,:], maph[:,0], maph[:,size-1] = (1,1,1,1)

    mapc[x][y], maph[x][y], mapr[x][y] = (0, 0, 0)
    count = 0 
    while 1:
        testx, testy = (x, y)
        if np.random.uniform() > 0.5:
            testx = testx + np.random.choice([-1, 1])
        else:
            testy = testy + np.random.choice([-1, 1])
        if testx > 0 and testx < size -1 and testy > 0 and testy < size -1:
            if maph[testx][testy] == 0 or count > 5:
                count = 0
                x, y = (testx, testy)
                mapc[x][y], maph[x][y], mapr[x][y] = (0, 0, 0)
                if x == size-2:
                    ex, ey = (x, y)
                    break
            else:
                count = count+1
    return np.asarray(mapc), np.asarray(maph), np.asarray(mapr), ex, ey

def rotation(rot, last_mouse): # for 1080p screen
    with mouse.Controller() as check:
        position = check.position
        if position[0] != last_mouse[0] or position[0]>1860 or position[0] < 60:
            delta = last_mouse[0] - position[0]
            if position[0]>1860:
                delta = 1860 - position[0]
            if position[0] < 60:
                delta = 60 - position[0]

            rot = rot + 4*np.pi*(0.5-delta/1920)


    return(rot, position)

def on_press(key_new):
    global key
    key = key_new
    
def movement(posx, posy, rot, maph):
    global key
    x, y = (posx, posy)
    keyout = None
    if key is not None:
        if key == keyboard.Key.up:
            x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
        elif key == keyboard.Key.down:
            x, y = (x - 0.3*np.cos(rot), y - 0.3*np.sin(rot))
        elif key == keyboard.Key.left:
            rot = rot - np.pi/8
        elif key == keyboard.Key.right:
            rot = rot + np.pi/8
        elif key == keyboard.Key.esc:
            keyout = 'esc'
    key = None        
    if maph[int(x)][int(y)] == 0:
        posx, posy = (x, y)
        
    return posx, posy, rot, keyout

def caster(x, y, i, ex, ey, maph, mapc, sin, cos, n, half, tx, ty, tc):
    while True: # ray loop
        xx, yy = (x, y)
        x, y = (x + cos, y + sin)
        n = n+1
        if half == None and int(x*2)%2 == int(y*2)%2:#(abs(int(3*xx)-int(3*x)) > 0 or abs(int(3*yy)-int(3*y))>0):
            tx.append(i)
            ty.append(-1/(0.04 * n*np.cos(np.deg2rad(i - 30))))
            if int(x) == ex and int(y) == ey:
                tc.append('b')
            else:
                tc.append('k')
        if maph[int(x)][int(y)] == 1 or (maph[int(x)][int(y)] == 0.5 and half == None):
            h , c = shader(n, maph, mapc, sin, cos, x, y, i)
            if maph[int(x)][int(y)] == 0.5 and half == None:
                half = [h, c, n]
            else:
                break

    return(c, h, x, y, n, half, tx, ty, tc)

def shader(n, maph, mapc, sin, cos, x, y, i):
    h = np.clip(1/(0.04 * n*np.cos(np.deg2rad(i-30))), 0, 1)
    c = np.asarray(mapc[int(x)][int(y)])*(0.4 + 0.6 * h)
    if maph[int(x+cos)][int(y-sin)] > 0.5:
        c = 0.85*c
        if maph[int(x-cos)][int(y+sin)] != 0 and sin >0:
            c = 0.7*c
    return h, c

def reflection(x, y, i, ex, ey, maph, mapc, sin, cos, n, c, h, half, tx, ty, tc):
    if half != None:
        plt.vlines(i, 0, h, lw = 8, colors = c, alpha=0.5) #top reflected
        plt.vlines(i, -half[0], 0, lw = 8, colors = half[1])# bottom regular
    else:
        plt.vlines(i, -h, h, lw = 8, colors = c, alpha=0.5) # draw vertical lines
    if maph[int(x+cos)][int(y-sin)] != 0:
        cos = -cos
    else:
        sin = -sin
    c2, h, x, y, n, half2, tx, ty, tc = caster(x, y, i, ex, ey, maph, mapc, sin, cos, n, half, tx, ty, tc)
    c = (c + c2)/2
    if half != None:
        plt.vlines(i, 0, h, lw = 8, colors = c) # draw vertical lines
    else:
        plt.vlines(i, -h, h, lw = 8, colors = c) # draw vertical lines
        if half2 !=  None:
            plt.vlines(i, -half2[0], 0, lw = 8, colors = half2[1])        
    return c, h, x, y, n, half2, tx, ty, tc     

if __name__ == '__main__':
    main()

```

</details>

 
 
<img src="https://avatars.githubusercontent.com/u/73144499?v=4" width="100" height="100">