from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')

linha = [
  [sg.Button('Abrir DaveTheDiver', key='dave'), [sg.Button('Abrir Player de Música', key='player')]],
  [sg.Button('Abrir App de tarefas', key='tarefas')]
]


layout =  [
  [sg.Frame('Bots',layout=linha, key='container')],
  [sg.Button('Sair')]
]
#janela
window= sg.Window('Tela de Apps', layout=layout)
#ler os eventos
while True:
  eventos, valores = window.read()
  if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
    break
  if eventos == 'dave':
    import DaveTheDiver
    DaveTheDiver.main()
  if eventos == 'tarefas':
    import apptarefas
    apptarefas.main()
    
  