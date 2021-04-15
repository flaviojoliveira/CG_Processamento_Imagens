# Execute os passos abaixo para peparação do ambiente de nosso laboratório

1. Crie um novo diretório denominado projeto-07

2. Abra este diretório em seu editor de código (VSCode)

3. Abrir o item de menu Terminal no VSCode

4. Com o terminal do VScode aberto inserir o seguinte comando:

*este comando cria um ambiente virtual python denominado "top"*
```
python3 -m venv top
```
5. Ativar o ambiente virtual criado

```
.\top\Scripts\Activate.ps1
```
*powershell no vscode*

ou
```
.\top\Scripts\Activate.bat
```
*CMD no vscode

##### Caso ocorra erro no criação de seu ambiente virtual W10

*ver dicas no grupo.*
Abrir powershell como administrador e executar o comando abaixo e em seguida responder S para sim.

```
 Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

6. Instalar as seguintes bibliotecas

Numpy, Matplotlib e Keyboard
```
pip install numpy
pip install matplotlib
pip install keyboard

```