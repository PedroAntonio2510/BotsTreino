from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout =  [
  [sg.Text('Bots Python', size=(20, 1))],
  [sg.Button('Abrir DaveTheDiver', key='dave')],
  [sg.Button('Sair')]
]
#janela
janela = sg.Window('Tela de Bots', layout)
#ler os eventos
while True:
  eventos, valores = janela.read()
  if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
    break
  if eventos == 'dave':
    import DaveTheDiver
    DaveTheDiver.main()