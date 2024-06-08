from PySimpleGUI import PySimpleGUI as sg
import os
from funcoes import *

sg.theme('reddit')

song_title_column = [
  [sg.Text('Que pais é este?', background_color='white', auto_size_text=True, text_color='black', font='Roboto',)]
]

PLAY_BUTTON_PLAY = '/Users/pedrinho/Bots/imagens/playButton.png'
FORWARD_BUTTON_PATH = '/Users/pedrinho/Bots/imagens/forwardButton.png'
BACKWARD_BUTTON_PATH = '/Users/pedrinho/Bots/imagens/backwardBtn.png'
PAUSE_BUTTON_PATH = '/Users/pedrinho/Bots/imagens/pauseButton.png'
ALBUM_COVER_MUSICA_PATH = '/Users/pedrinho/Bots/imagens/legiaoUrbana.png'



main = [
  [sg.Canvas(background_color='white', size=(480, 80), pad=None)],
  [sg.Canvas(background_color='white', size=(40, 350)), sg.Image(
      filename=ALBUM_COVER_MUSICA_PATH, size=(350, 350), pad=None),
    sg.Canvas(background_color='white', size=(40, 350), pad=None)],
  [sg.Canvas(background_color='white', size=(480, 15))],
  [sg.Column(song_title_column, background_color='white', justification='c', element_justification='c')],
  [sg.Canvas(background_color='white', size=(0, 10))],
  [sg.HorizontalSeparator(color='black')],
  [
    sg.Canvas(background_color='white',
               size=(128, 200), pad=None), 
    sg.Image(filename= BACKWARD_BUTTON_PATH,
              size=(35,44), pad=None), 
    sg.Image(filename= PLAY_BUTTON_PLAY,
              size=(64, 64), enable_events=True,pad=None, key='play'), 
    sg.Image(filename=PAUSE_BUTTON_PATH, 
             enable_events=True, pad=None, key='pause', size=(64,64)),
    sg.Image(filename= FORWARD_BUTTON_PATH,
              size=(35, 44), pad=None), 
    sg.Canvas(background_color='white', size=(128,200), pad=None)
  ]
]

window = sg.Window('App em python', layout=main, size=(480, 700))

while True:
  eventos, valores =  window.read()
  if eventos == sg.WINDOW_CLOSED:
    break
  elif eventos == 'play':
    directory = '/Users/pedrinho/Bots/musicas/legiao.wav'
    if is_playing_sound():
      pass
    if is_playing_sound() == False:
      play_sound(directory)
  elif eventos == 'pause':
    if is_playing_sound():
      pause()
    else:
      unpause()
    pass