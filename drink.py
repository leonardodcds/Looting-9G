from random import randint

def drink():

  # Gerar Bebida:
  d = randint(0, 5)
  drk = [
    'Garrafa de Aguardente',
    'Garrafa de Cerveja   ',
    'Garrafa de Grappa    ',
    'Garrafa de Hidromel  ',
    'Garrafa de Pinganã   ',
    'Garrafa de Vinho     ',
  ]
  print('║ ╔═════════════════════════════╗ ║')
  print('║ ║            Geral            ║ ║')
  print('║ ║ > ' + drk[d] + '     ║ ║')
  print('║ ╚═════════════════════════════╝ ║')