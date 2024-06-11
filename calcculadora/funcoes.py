
def process_number(eventos, current_number):
  current_number += eventos
  return current_number

def operacoes(first_number, second_number, operation):
  if operation == '+':
    return first_number + second_number
  elif operation == '-':
    return first_number - second_number
  elif operation == 'X':
    return first_number * second_number
  elif operation == '/':
    return first_number / second_number if second_number !=- 0 else 'Erro'
    
def reset():
  return '', None, None


