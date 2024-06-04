#Bot para abrir o jogo Dave The Diver no meu dispositivo

import pyautogui, time
pyautogui.PAUSE = 2

def abrir_steam():
  pyautogui.hotkey('option','space', interval=0.1)
  pyautogui.write('steam')
  pyautogui.hotkey('return')
def abrir_jogo():
  pyautogui.moveTo(x=533, y=197)
  pyautogui.click()
  time.sleep(3)
  pyautogui.moveTo(x=468, y=330)
  time.sleep(1)
  pyautogui.click()
  time.sleep(2)
  pyautogui.write('dave', interval=1)
  pyautogui.moveTo(x=471, y=392)
  pyautogui.click(button='right')
  time.sleep(1)
  pyautogui.moveTo(x=570, y=413)
  time.sleep(0.5)
  pyautogui.click()

def main():
  abrir_steam()
  time.sleep(20)
  abrir_jogo()

if __name__ == '__main__':
  main()


# Posicao da bilbioteca --> x=533, y=197
# Posicao da pesquisa --> x=468, y=330
# Posicao do jogo --> x=471, y=392
# posicao jogar --> x=570, y=413