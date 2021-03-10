from random import randint

def up():

  # Gerar Bebida:
  p = randint(1, 23)
  u = [
    'Pontos de Vida          ',
    'Pontos de Mana          ',
    'Defesa Física           ',
    'Velocidade              ',
    'Defesa Mágica           ',
    'Atributo de Ataque      ',
    'Atributo de Precisão    ',
    'Atributo de Feitiçaria  ',
    'Atributo de Vigor       ',
    'Atributo de Agilidade   ',
    'Atributo de Destreza    ',
    'Atributo de Sabedoria   ',
    'Atributo de Inteligência',
    'Atributo de Carisma     ',
    'Atributo de Ofício      ',
    'Perícia de Vigor        ',
    'Perícia de Agilidade    ',
    'Perícia de Destreza     ',
    'Perícia de Sabedoria    ',
    'Perícia de Inteligência ',
    'Perícia de Carisma      ',
    'Magia Duplicada         ',
    'Magia Dividida          '
  ]
  print('║ ╔═════════════════════════════╗ ║')
  print('║ ║           Upgrade           ║ ║')
  print('║ ║ > ' + u[p-1] + '  ║ ║')
  print('║ ╚═════════════════════════════╝ ║')