from PySimpleGUI import PySimpleGUI as sg

def criar_janela():
  sg.theme('Python')

  linha = [
    [sg.Checkbox(''), sg.Input('')]
  ]

  layout = [
    [sg.Frame('Tarefas', layout=linha, key='container') ],
    [sg.Button('Nova tarefa'), sg.Button('Resetar')]
  ]

  return sg.Window('To-do list', layout=layout, finalize=True)
window = criar_janela()

while True:
  eventos, valores = window.read()
  if eventos == sg.WINDOW_CLOSED:
    break
  if eventos == 'Nova tarefa':
    window.extend_layout(window['container'], [[sg.Checkbox(''), sg.Input('')]])
  if eventos == 'Resetar':
    window.close() 
    window = criar_janela()

   