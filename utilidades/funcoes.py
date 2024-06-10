import os
from pygame import mixer
mixer.init()


def get_files_inside_directory_not_recursive(directory):
  directories = []
  for entry in os.listdir(directory):
     entry_path = os.path.join(directory, entry)
     if os.path.isdir(entry_path):
        directories.append(entry_path)
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
  return mixer.music.get_busy()