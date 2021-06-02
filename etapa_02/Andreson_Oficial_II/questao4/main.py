import PySimpleGUI as sg

#layout
sg.theme('Reddit')
def janela_logo():
    
    layout = [[sg.Image(r'questao4\ascentes\cantina.png')],
            [sg.Button('Entrar')]
    ]
    return sg.Window('logo', layout=layout, finalize=True)

def janela_pedido():
    #sg.theme('Reddit')
    layout = [
        [sg.Text('fazer pedido')]
    ]
    return sg.Window('menu', layout=layout, finalize=True)

def janelar_pagar():
    layout = [
        [sg.Text('pagar')]
    ]
#janela
#janela = sg.Window('login', layout)
janela1, janela2 = janela_logo(), None
#ler os eventos
while True:
   janela, eventos, valores = sg.read_all_windows()
   if eventos == sg.WINDOW_CLOSED:
       break
   if janela == janela1 and eventos == 'Entrar':
       janela2 = janela_pedido()
       janela1.hide()