from PySimpleGUI import PySimpleGUI as sg
import speedtest

st = speedtest.Speedtest()

def criar_layout():
  sg.theme('Reddit')
  titulo = [
    [sg.Text('Test Internet Speed',font='Roboto 30 bold'
  )]
  ]

  linha2 = [
    [sg.Text('⏬ Download Speed - ', font='Roboto 15 bold'), sg.Text(size=(50,1), key='DOWNLOAD', font='Courier 14')],
    [sg.Text('⏫ Upload Speed - ', font='Roboto 15 bold'), sg.Text(size=(50, 1), key='UPLOAD', font='Courier 14')],
    [sg.Text('Your Ping is - ',font='Roboto 15 bold'), sg.Text(size=(50, 1), key='PING', font='Courier 14')]
  ]


  main = [
    [sg.Column(layout=titulo, justification='c', element_justification='c')],
    [sg.Column(layout=linha2, justification='c', element_justification='c')],
    [sg.Canvas(background_color='white', size=(130, 10)),
    sg.Button('Check Speed'),
    sg.Canvas(background_color='white', size=(190, 10))]
  ]

  return sg.Window('Test internet speed', layout=main, icon='speed.ico', size=(380,260))


def check_speed():
  global download_speed, upload_speed
  speed_test= speedtest.Speedtest()
  download= speed_test.download()
  upload = speed_test.upload()

  download_speed = round(download / (10 ** 6), 2)
  upload_speed = round(upload / (10 ** 6), 2)
    

def mudar_layout():
  check_speed()
  window['DOWNLOAD'].update(f'{download_speed:.2f}Mbps')
  window['UPLOAD'].update(f'{upload_speed:.2f}Mbps')
  # Pegar ping
  servernames = []
  st.get_servers([])
  ping = st.results.ping
  
  window['PING'].update(f'{ping}')
    
window = criar_layout()
def main():
  while True:
    events, valores = window.read()
    if events == sg.WINDOW_CLOSED:
      sg.popup('Programa encerrado')
      break
    if events == 'Check Speed':
      mudar_layout()

if __name__ == '__main__':
  main()