from PySimpleGUI import PySimpleGUI as sg

sg.theme('reddit')

song_title_column = [
  [sg.Text('Legião Urbana', background_color='white', auto_size_text=True, text_color='black', font='Roboto')]
]

main = [
  [sg.Canvas(background_color='white', size=(580, 100), pad=None)],
  [sg.Canvas(background_color='white', size=(100, 500), pad=None), sg.Image(filename='/Users/pedrinho/Bots/imagens/legiaoUrbana.png')],
  [sg.Canvas(background_color='white', size=(500, 10), pad=None)],
  [sg.Column(song_title_column, background_color='white', justification='c', element_justification='c')],
  [sg.Canvas(background_color='white', size=(100, 200), pad=10), sg.Image(pad=(10,0),filename= '/Users/pedrinho/Bots/imagens/backwardBtn.png'), sg.Image(pad=(38,0),filename= '/Users/pedrinho/Bots/imagens/playButton.png'), sg.Image(pad=(10,0),filename= '/Users/pedrinho/Bots/imagens/forwardButton.png')],
]

window = sg.Window('Spotirola', main)

while True:
  eventos, valores =  window.read()
  if eventos == sg.WINDOW_CLOSED:
    break