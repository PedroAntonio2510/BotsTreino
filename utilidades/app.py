from PySimpleGUI import PySimpleGUI as sg
import os
from utilidades.funcoes import *

sg.theme('reddit')

song_title_column = [
  [sg.Text('De o play...', background_color='white', auto_size_text=True, text_color='black', font='Roboto',)]
]

currently_playing = [
  [sg.Text(background_color='white', size=(200, 0), text_color='black',
            font=('Tahoma', 10), key='currently_playing')]
]


PLAY_BUTTON_PLAY = '/Users/pedrinho/Bots/utilidades/imagens/playButton.png'
FORWARD_BUTTON_PATH = '/Users/pedrinho/Bots/utilidades/imagens/forwardButton.png'
BACKWARD_BUTTON_PATH = '/Users/pedrinho/Bots/utilidades/imagens/backwardBtn.png'
PAUSE_BUTTON_PATH = '/Users/pedrinho/Bots/utilidades/imagens/pauseButton.png'
ALBUM_COVER_MUSICA_PATH = '/Users/pedrinho/Bots/utilidades/imagens/legiaoUrbana.png'



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
              size=(35,44), pad=None, key='previous', enable_events=True), 
    sg.Image(filename= PLAY_BUTTON_PLAY,
              size=(64, 64), enable_events=True,pad=None, key='play'), 
    sg.Image(filename=PAUSE_BUTTON_PATH, 
             enable_events=True, pad=None, key='pause', size=(64,64)),
    sg.Image(filename= FORWARD_BUTTON_PATH,
              size=(35, 44), pad=None, key='next', enable_events=True), 
    sg.Canvas(background_color='white', size=(128,200), pad=None)
  ],
  [
    sg.Column(layout=currently_playing, justification='c', element_justification='c', background_color='black', pad=None)
  ]
]

def update_display():
  if 0 <= current_song_index < song_count:
    window['song_name'].update(os.path.basename(songs_in_directory[current_song_index]))
    window['currently_playing'].update(f'Playing: {os.path.basename(songs_in_directory[current_song_index])}')

def next_song():
    if current_song_index + 1 < song_count:
      stop()
      current_song_index += 1
      play_sound(songs_in_directory[current_song_index])
      update_display()

window = sg.Window('App em python', layout=main, size=(480, 700), background_color='white', finalize=True, grab_anywhere=True, resizable=False)

directory = sg.popup_get_folder('Selecione o diretorio: ')
print("Diretorio selecionado: ", directory)
songs_in_directory = get_files_inside_directory_not_recursive(directory)
song_count = len(songs_in_directory)
current_song_index = 0

while True:
  eventos, valores =  window.read()
  if eventos == sg.WINDOW_CLOSED:
    break
  elif eventos == 'play':
    if not is_playing_sound():
      play_sound(songs_in_directory)
  elif eventos == 'pause':
    if is_playing_sound():
      pause()
    else:
      unpause()
    pass
  elif eventos == 'next':
    next_song()
