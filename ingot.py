from random import randint

def ingot():

  # Gerar Barra:
  i = randint(0, 9)
  ing = [
    'Barra de Cobre  ',
    'Barra de Bronze ',
    'Barra de Níquel ',
    'Barra de Estanho',
    'Barra de Ferro  ',
    'Barra de Prata  ',
    'Barra de Eletro ',
    'Barra de Ouro   ',
    'Barra de Platina',
    'Barra de Mitral ' 
  ]
  print('║ ╔═════════════════════════════╗ ║')
  print('║ ║            Geral            ║ ║')
  print('║ ║ > ' + ing[i] + '          ║ ║')
  print('║ ╚═════════════════════════════╝ ║')