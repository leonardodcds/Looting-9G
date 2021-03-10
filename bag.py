from random import randint

def bag():

  # Gerar Item:
  m = randint(1, 57)
  ite = [
    'Algema       ',
    'Ampulheta    ',
    'Anzol        ',
    'Armadilha    ',
    'Balde        ',
    'Baralho      ',
    'Barril       ',
    'Baú          ',
    'Bigorna P    ',
    'Bigorna M    ',
    'Bigorna G    ',
    'Bússola      ',
    'Caneca       ',
    'Caneta       ',
    'Cantil       ',
    'Carimbo      ',
    'Chifre       ',
    'Corda (1m)   ',
    'Couro P      ',
    'Couro M      ',
    'Couro G      ',
    'Dado         ',
    'Elixir       ',
    'Escamas P    ',
    'Escamas M    ',
    'Escamas G    ',
    'Frasco       ',
    'Gancho       ',
    'Garra        ',
    'Garrafa      ',
    'Gazua        ',
    'Grimório     ',
    'Guampa       ',
    'Jarro        ',
    'Lampião      ',
    'Livro        ',
    'Lunadorno    ',
    'Luneta       ',
    'Mapa         ',
    'Pá           ',
    'Panela       ',
    'Papel        ',
    'Pé de Cabra  ',
    'Pederneira   ',
    'Pergaminho   ',
    'Picareta     ',
    'Poção        ',
    'Prego        ',
    'Presa        ',
    'Ração        ',
    'Rede de Pesca',
    'Saco         ',
    'Sineta       ',
    'Tenda        ',
    'Tocha        ',
    'Vara de Pesca',
    'Xadrez       '
  ]
  print('║ ╔═════════════════════════════╗ ║')
  print('║ ║            Geral            ║ ║')
  print('║ ║ > ' + ite[m-1] + '             ║ ║')
  print('║ ╚═════════════════════════════╝ ║')