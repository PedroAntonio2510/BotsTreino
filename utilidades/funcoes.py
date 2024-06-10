import os
from pygame import mixer
mixer.init()


def get_files_inside_directory_not_recursive(directory):
  directories = []
  for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
      directories.append(file_path)

  return directories


def play_sound(sound_path):
  mixer.music.load(sound_path)
  mixer.music.play()

def stop():
  mixer.music.stop()

def pause():
  mixer.music.pause()

def unpause():
  mixer.music.unpause()

def is_playing_sound():
  if mixer.music.get_busy() == True:
        return True
  return False
