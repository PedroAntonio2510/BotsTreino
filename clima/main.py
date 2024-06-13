from PySimpleGUI import PySimpleGUI as sg
import requests


def get_weather(city):
    api_key = "a4aa5e3d83ffefaba8c00284de6ef7c3"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def criar_layout():
  sg.theme('Reddit')

  linha = [
    [sg.Input(key='-CITY-'), sg.Button('Buscar')]
  ]
  linha2 = [
    [sg.Text('Cidade: ', font='Roboto 15 bold'), sg.Text(key='city', font='Roboto 15')],
    [sg.Text('Condições:', font='Roboto 15 bold'), sg.Text(key='conditions', font='Roboto 15 ')],
    [sg.Text('Temperatura: ', font='Roboto 15 bold'), sg.Text(key='temperature', font='Roboto 15 ')]

  ]

  main = [
    [sg.Column(layout=linha, justification='c')],
    [sg.Column(layout=linha2, justification='c', pad=(0, 10))]
  ]

  return sg.Window('Verificador de clima', layout=main, finalize=True, size=(500, 200))

def main():
  window = criar_layout()
  
  while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
      break
    if eventos == 'Buscar':
      city = valores['-CITY-']
      if city:
        weather = get_weather(city)
        if weather.get('cod') == 200:
          description = weather['weather'][0]['description']
          temp = weather['main']['temp']
          window['city'].update(f'{city}')
          window['conditions'].update(f'{description}')
          window['temperature'].update(f'{temp}°C')
        else:
          result = "Cidade não encontrada."
          sg.Popup(result)
if __name__ == "__main__":
  main()