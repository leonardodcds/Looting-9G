from colored import fg, bg, attr
from random import randint
import termcolor as c

def spell():

  # Gerar Runa
  ctgr = randint(1, 18)
  if ctgr == 1:
    runa = c.colored('Ignis ', 'red', attrs=['bold'])
    tipo = 'de Fogo  '
    dano = 'ígneo   '
    base = '1d6 '
  elif ctgr == 2:
    runa = c.colored('Radii ', 'yellow', attrs=['bold'])
    tipo = 'de Raio  '
    dano = 'elétrico'
    base = '1d8 '
  elif ctgr == 3:
    runa = c.colored('%sLumen %s' % (fg(11), attr(0)), attrs=['bold'])
    tipo = 'de Luz   ' 
    dano = 'lúmino  '
    base = '1d4 '
  elif ctgr == 4:
    runa = c.colored('Terra ', 'green', attrs=['bold'])
    tipo = 'de Terra '
    dano = 'sísmico '
    base = '1d10'
  elif ctgr == 5:
    runa = c.colored('%sAquae %s' % (fg(51), attr(0)), attrs=['bold'])
    tipo = 'de Água  '
    dano = 'áqueo   '
    base = '1d6 '
  elif ctgr == 6:
    runa = c.colored('%sGelum %s' % (fg(27), attr(0)), attrs=['bold'])
    tipo = 'de Gelo  '
    dano = 'gélido  '
    base = '1d8 '
  elif ctgr == 7:
    runa = c.colored('%sUmbra %s' % (fg(129), attr(0)), attrs=['bold'])
    tipo = 'de Treva '
    dano = 'úmbreo  '
    base = '1d12'
  elif ctgr == 8:
    runa = c.colored('%sVento %s' % (fg(201), attr(0)), attrs=['bold'])
    tipo = 'de Vento '
    dano = 'zéphiro '
    base = '1d4 '
  elif ctgr == 9:
    runa = c.colored('%sArcan %s' % (fg(243), attr(0)), attrs=['bold'])
    tipo = 'de Éter  '
    dano = 'arcano  '
    base = '2d4 '
  elif ctgr == 10:
    runa = c.colored('Comba ', 'red', attrs=['bold'])
  elif ctgr == 11:
    runa = c.colored('Divina', 'yellow', attrs=['bold'])
  elif ctgr == 12:
    runa = c.colored('%sHarmo %s' % (fg(11), attr(0)), attrs=['bold'])
  elif ctgr == 13:
    runa = c.colored('Morph ', 'green', attrs=['bold'])
  elif ctgr == 14:
    runa = c.colored('%sAbjur %s' % (fg(51), attr(0)), attrs=['bold'])
  elif ctgr == 15:
    runa = c.colored('%sIlusio%s' % (fg(27), attr(0)), attrs=['bold'])
  elif ctgr == 16:
    runa = c.colored('%sNecro %s' % (fg(129), attr(0)), attrs=['bold'])
  elif ctgr == 17:
    runa = c.colored('%sEncan %s' % (fg(201), attr(0)), attrs=['bold'])
  elif ctgr == 18:
    runa = c.colored('%sAnima %s' % (fg(243), attr(0)), attrs=['bold'])

  # Gerar Tipo:
  if ctgr <= 9:
    t = randint(1, 15)
    if t >= 11:
      nome = 'Soco ' + tipo
      dscc = 'um alvo adjacente        '
      sc = base.split('d')
      if sc[0] == '1':
        base = '2d' + sc[1]
      elif sc[0] == '2':
        base = '3d' + sc[1]
    elif t >= 7:
      nome = 'Bola ' + tipo
      dscc = 'o alvo e suas adjacências'
    elif t >= 4:
      nome = 'Seta ' + tipo
      dscc = 'uma linha inimiga        '
    elif t >= 2:
      nome = 'Onda ' + tipo
      dscc = 'uma coluna inimiga       '
    elif t == 1:
      nome = 'Cone ' + tipo
      dscc = 'um V no campo inimigo    '

  # Gerar Magia Elemental:
  if ctgr <= 9:
    print('║ ╔═════════════════════════════╗ ║')
    print('║ ║            Magia            ║ ║')
    print('║ ║ Runa:                       ║ ║')
    print('║ ║ >', runa, '                   ║ ║')
    print('║ ║   └', nome, '         ║ ║')
    print('║ ╟─────────────────────────────╢ ║')
    print('║ ║ Dano:                       ║ ║')
    if base == '1d10' or base == '1d12' or base == '2d10' or base == '2d12':
      print('║ ║ └ '+ base + ' de dano ' + dano + '     ║ ║')
    else:
      print('║ ║ └ ' + base + 'de dano ' + dano + '      ║ ║')
    print('║ ║ Área:                       ║ ║')
    print('║ ║ └ ' + dscc + ' ║ ║')
    print('║ ╚═════════════════════════════╝ ║')

  # Gerar Magia Hermética:
  else:
    print('║ ╔═════════════════════════════╗ ║')
    print('║ ║            Magia            ║ ║')
    print('║ ║ Runa:                       ║ ║')
    print('║ ║ >', runa, '                   ║ ║')
    print('║ ║   └ ∙∙∙                     ║ ║')
    print('║ ╚═════════════════════════════╝ ║')