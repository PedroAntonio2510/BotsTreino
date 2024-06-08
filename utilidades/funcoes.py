import os
from pygame import mixer
mixer.init()

path = '/Users/pedrinho/Bots/utilidades/musicas/legiao.wav'

def pegar_arquivo(directory):
  directories = []
  for (root, dirs, files) in os.walk(directory):
    for file in files:
      directories.append(root + os.sep + file)

def play_sound(directory):
  mixer.music.load(directory)
  mixer.music.play()

def stop():
  mixer.music.stop()

def pause():
  mixer.music.pause()

def unpause():
  mixer.music.unpause()

def is_playing_sound():
  return mixer.music.get_busy()

