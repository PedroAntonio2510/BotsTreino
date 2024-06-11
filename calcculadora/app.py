from PySimpleGUI import PySimpleGUI as sg
from funcoes import process_number, operacoes, reset

sg.theme('LightBlue6')
def create_window():
  linha = [
    [sg.Input('', size=(20), justification='right', key='display')]
  ] 

  linha2 = [
    [sg.Button('7'),
    sg.Button('8'),
      sg.Button('9')
    ]
  ]

  linha3 = [
    [sg.Button('4'),
    sg.Button('5'),
      sg.Button('6')]
  ]

  linha4 = [
    [sg.Button('1'),
    sg.Button('2'),
      sg.Button('3')]
  ]

  linha5 = [
    [sg.Button('C'),
    sg.Button('0'),
    sg.Button('AC')]
  ]

  main = [
    [sg.Frame(' ',layout=linha)],
    [sg.Column(layout=linha2, pad=5), sg.Button('X', size=2)],
    [sg.Column(layout=linha3), sg.Button('/', size=2)],
    [sg.Column(layout=linha4), sg.Button('+', size=2)],
    [sg.Column(layout=linha5), sg.Button('-', size=2), sg.Button('=')]
  ]
  return sg.Window('Calculdaora', layout=main)

def main():
  window = create_window()

  current_number = ''
  result = 0

  while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
      break
    elif eventos in '0123456789':
      current_number += eventos
      window['display'].update(current_number)
    elif eventos in '+-X/':
      first_number = float(current_number)
      operation = eventos
      current_number = ''
    elif eventos == '=':
      if first_number is not None and current_number != 0:
        second_number = float(current_number)
        result = operacoes(first_number, second_number, operation)
        current_number = str(result)
        window['display'].update(result)
        first_number = None
        operation = None
    elif eventos == 'C':
      current_number, first_number, operation = reset()
      window['display'].update('')
    
if __name__ == '__main__':
  main()