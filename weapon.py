from colored import fg, bg, attr
from random import randint
import termcolor as c

def weapon():

  # Gerar Discode (0 - Não / 1 - Sim)
  dscd = 0

  # Gerar Categoria e Tier:
  ctgr = randint(1, 19)
  if ctgr <= 16:
    tier = randint(1, 3)
  elif ctgr == 17 or ctgr == 18:
    tier = randint(1, 4)
  elif ctgr == 19:
    tier = randint(1, 8)

  # Gerar Arma/Dano:
  if ctgr == 1:    # MACHADOS
    clss = 'MAC'
    if tier == 1:
      arma = 'Hache       '
      dano = '2d4'
    elif tier == 2:
      arma = 'Lenho       '
      dano = '2d6'
    else:
      arma = 'Machado     '
      dano = '2d8'
  elif ctgr == 2:  # ESPADINS
    clss = 'ISP'
    if tier == 1:
      arma = 'Dardo       '
      dano = '1d4'
    elif tier == 2:
      arma = 'Adaga       '
      dano = '1d6'
    else:
      arma = 'Facão       '
      dano = '1d6'
  elif ctgr == 3:  # ESPADAS
    clss = 'ESP'
    if tier == 1:
      arma = 'Espada Curta'
      dano = '1d8'
    elif tier == 2:
      arma = 'Espada Média'
      dano = '1d10'
    else:
      arma = 'Espada Longa'
      dano = '1d12'
  elif ctgr == 4:  # KATANAS
    clss = 'KAT'
    if tier == 1:
      arma = 'Nagaw       '
      dano = '1d8'
    elif tier == 2:
      arma = 'Katana      '
      dano = '2d8'
    else:
      arma = 'Odachi      '
      dano = '3d8'
  elif ctgr == 5:  # SABRES
    clss = 'SAB'
    if tier == 1:
      arma = 'Sabre       '
      dano = '1d8'
    elif tier == 2:
      arma = 'Baioneta    '
      dano = '1d10'
    else:
      arma = 'Rapieira    '
      dano = '1d12'
  elif ctgr == 6:  # LANÇAS
    clss = 'LAN'
    if tier == 1:
      arma = 'Pique       '
      dano = '1d6'
    elif tier == 2:
      arma = 'Lança       '
      dano = '2d6'
    else:
      arma = 'Alabarda    '
      dano = '3d6'
  elif ctgr == 7:  # FOICES
    clss = 'FOI'
    if tier == 1:
      arma = 'Foice Curta '
      dano = '1d8'
    elif tier == 2:
      arma = 'Foice Longa '
      dano = '2d6'
    else:
      arma = 'Kusarigamas '
      dano = '4d4'
  elif ctgr == 8:  # RÚNIOS
    clss = 'RUN'
    if tier == 1:
      arma = 'Varinha     '
      dano = ''
    elif tier == 2:
      arma = 'Cajado      '
      dano = ''
    else:
      arma = 'Cetro       '
      dano = ''
  elif ctgr == 9:  # MARTELOS
    clss = 'MAR'
    if tier == 1:
      arma = 'Malho       '
      dano = '2d4'
    elif tier == 2:
      arma = 'Martelo     '
      dano = '3d4'
    else:
      arma = 'Marreta     '
      dano = '4d4'
  elif ctgr == 10: # BASTÕES
    clss = 'BAS'
    if tier == 1:
      arma = 'Bordão      '
      dano = '1d4'
    elif tier == 2:
      arma = 'Bastão      '
      dano = '1d8'
    else:
      arma = 'Tonfas      '
      dano = '2d8'
  elif ctgr == 11: # CLAVAS
    clss = 'CLA'
    if tier == 1:
      arma = 'Clava       '
      dano = '2d4'
    elif tier == 2:
      arma = 'Estrela     '
      dano = '2d6'
    else:
      arma = 'Mangual     '
      dano = '3d6'
  elif ctgr == 12: # RELHOS
    clss = 'REL'
    if tier == 1:
      arma = 'Relho       '
      dano = '1d4'
    elif tier == 2:
      arma = 'Flagelo     '
      dano = '3d4'
    else:
      arma = 'Chicote     '
      dano = '5d4'
  elif ctgr == 13: # BESTAS
    clss = 'BES'
    if tier == 1:
      arma = 'Besta       '
      dano = '1d6'
    elif tier == 2:
      arma = 'Balestra    '
      dano = '2d6'
    else:
      arma = 'Mosquete    '
      dano = '4d6'
  elif ctgr == 14: # ARCOS COMUNS
    clss = 'ARC'
    if tier == 1:
      arma = 'Arco Curto  '
      dano = '1d8'
    elif tier == 2:
      arma = 'Arco Médio  '
      dano = '1d10'
    else:
      arma = 'Arco Longo  '
      dano = '1d12'
  elif ctgr == 15: # ARCOS RÚNICOS
    clss = 'ARR'
    if tier == 1:
      arma = 'Arco Duplo  '
      dano = '2d4'
    elif tier == 2:
      arma = 'Arco Trino  '
      dano = '3d4'
    else:
      arma = 'Arco Tetro  '
      dano = '4d4'
  elif ctgr == 16: # INSTRUMENTOS
    clss = 'INS'
    if tier == 1:
      arma = 'Flauta      '
      dano = ''
    elif tier == 2:
      arma = 'Alaúde      '
      dano = ''
    else:
      arma = 'Tambor      '
      dano = ''
  elif ctgr == 17: # ESCUDOS
    item = 'Escudo'
    dffs = str(tier)
    dfmg = '0'
  elif ctgr == 18: # ADORNOS
    item = 'Adorno'
    dffs = '0'
    dfmg = str(tier)
  elif ctgr == 19: # ARMADURAS
    item = 'Armadura'
    dffs = str(tier - randint(0, tier))
    dfmg = str(tier - int(dffs))

  # Gerar Crítico:
  if ctgr == 5 or ctgr == 9 or ctgr == 10 or ctgr == 12 or ctgr == 14:
    crit = 'x2'
  elif ctgr <= 4 or ctgr == 6 or ctgr == 13:
    if tier <= 2:
      crit = 'x2'
    else:
      crit = 'x3'
  else:
    crit = 'x3'

  # Gerar Alcance:
  alcc = '{1}'
  if ctgr == 7 or ctgr == 12:
    if tier == 2:
      alcc = '{2}'
    elif tier == 3:
      alcc = '{3}'
  elif ctgr == 8 or ctgr == 14:
    if tier == 1:
      alcc = '{3}'
    elif tier == 2:
      alcc = '{4}'
    else:
      alcc = '{5}'
  elif ctgr == 13:
    alcc = '{3}'
  elif ctgr >= 15:
    alcc = '{4}'

  # Gerar Manuseio:
  hand = '(o)'     #ooo
  if ctgr == 1 or ctgr == 3 or ctgr == 4 or ctgr == 9: 
    if tier == 3:
      hand = '(d)' #ood
  elif ctgr == 7 or ctgr == 13: 
    if tier >= 2:
      hand = '(d)' #odd
  elif ctgr == 6 or ctgr == 10 or ctgr == 14 or ctgr == 15 or ctgr == 16: 
    hand = '(d)'   #ddd
  elif ctgr == 5 or ctgr == 12:
    if tier >= 2:
      hand = '(u)' #ouu
  elif ctgr == 8 or ctgr == 11:
    hand = '(u)'   #uuu

  # Gerar Material:
  m = randint(1, 100)
  if m >= 86:   # 15%
    m = 0
  elif m >= 73: # 13%
    m = 1
  elif m >= 61: # 12%
    m = 2
  elif m >= 50: # 11%
    m = 3
  elif m >= 40: # 10%
    m = 4
  elif m >= 31: # 09%
    m = 5
  elif m >= 23: # 08%
    m = 6
  elif m >= 16: # 07%
    m = 7
  elif m >= 10: # 06%
    m = 8
  elif m >= 5:  # 05%
    m = 9
  else:         # 04%
    m = 10
  mtrl = [
    'Liga   ',
    'Cobre  ',
    'Bronze ',
    'Níquel ',
    'Estanho',
    'Ferro  ',
    'Prata  ',
    'Eletro ',
    'Ouro   ',
    'Platina',
    'Mitral '
  ]

  # Gerar Raridade:
  r = randint(1, 100)
  if r >= 74:   # 27%
    r = 0
  elif r >= 52: # 22%
    r = 1
  elif r >= 34: # 18%
    r = 2
  elif r >= 20: # 14%
    r = 3
  elif r >= 10: # 10%
    r = 4
  elif r >= 4:  # 06%
    r = 5
  else:         # 03%
    r = 6
  rrdd = [
    c.colored('%s[C]%s' % (fg(243), attr(0)), attrs=['bold']),
    c.colored('%s[I]%s' % (fg(247), attr(0)), attrs=['bold']),
    c.colored('[U]', 'green', attrs=['bold']),
    c.colored('%s[R]%s' % (fg(27), attr(0)), attrs=['bold']),
    c.colored('%s[E]%s' % (fg(129), attr(0)), attrs=['bold']),
    c.colored('[H]', 'red', attrs=['bold']),
    c.colored('[L]', 'yellow', attrs=['bold'])
  ]

  # Gerar Bônus de Dano:
  if ctgr <= 16:
    if dano == '':
      if r == 1:
        dano = dano + c.colored('+1    ', 'green')
      elif r == 2:
        dano = dano + c.colored('+2    ', 'green')
      elif r >= 3:
        dano = dano + c.colored('+3    ', 'green')
      else:
        dano = dano + '      '
    elif dano == '1d10' or dano == '1d12':
      if r == 1:
        dano = dano + c.colored('+1', 'green')
      elif r == 2:
        dano = dano + c.colored('+2', 'green')
      elif r >= 3:
        dano = dano + c.colored('+3', 'green')
      else:
        dano = dano + '  '
    else:
      if r == 1:
        dano = dano + c.colored('+1 ', 'green')
      elif r == 2:
        dano = dano + c.colored('+2 ', 'green')
      elif r >= 3:
        dano = dano + c.colored('+3 ', 'green')
      else:
        dano = dano + '   '

  # Gerar Encantamento Épico:
  enc1 = [
    '∙                    ',
    c.colored('∙ Causa Dano Ígneo   ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Elétrico', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Lúmino  ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Sísmico ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Áqueo   ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Gélido  ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Úmbreo  ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Zéphiro ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Arcano  ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Psiquico', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Venenoso', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Sonoro  ', 'green', attrs=['bold']),
    c.colored('∙ Causa Dano Nécreo  ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Ígneo   ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Elétrico', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Lúmino  ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Sísmico ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Áqueo   ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Gélido  ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Úmbreo  ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Zéphiro ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Arcano  ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Psiquico', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Venenoso', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Sonoro  ', 'green', attrs=['bold']),
    c.colored('∙ Anula Dano Nécreo  ', 'green', attrs=['bold']) 
  ]
  e1 = 0
  if r >= 4:
    if ctgr <= 16:
      e1 = randint(1, 13)
    elif ctgr >= 17:
      e1 = randint(14, 26)

  # Gerar Encantamento Épico:
  enc2 = '∙                      '
  if r >= 5:
    enc2 = c.colored('∙ Encantamento Heroico ', 'red', attrs=['bold'])

  # Gerar Encantamento Lendário:
  enc3 = '∙                      '
  if r == 6:
    enc3 = c.colored('∙ Encantamento Lendário', 'yellow', attrs=['bold'])

  # Gerar Resistência:
  if ctgr >= 17 and ctgr <= 19:
    if r == 0:
      rstc = '(o)'  
    elif r == 1:
      rstc = c.colored('1d4', 'green') 
    elif r == 2:
      rstc = c.colored('1d6', 'green')
    elif r >= 3:
      rstc = c.colored('1d8', 'green')


  # Print - Armas
  if ctgr <= 16:
    print('║ ╔═════════════════════════════╗ ║')
    print('║ ║            Ficha            ║ ║')
    print('║ ║ Arma:                  ',rrdd[r],'║ ║')
    print('║ ║ >', arma, '             ║ ║')
    if m != 0:
      print('║ ║   └ ornado com', mtrl[m], '     ║ ║')
    else:
      print('║ ║   └ ∙∙∙                     ║ ║')    
    print('║ ╟─────────────────────────────╢ ║')
    print('║ ║           TIER:', tier,'          ║ ║')
    print('║ ╟──────────────┬──────────────╢ ║')
    print('║ ║ Dano:', dano,'│ Crítico: d' + crit,'║ ║')
    print('║ ║ Hand:', hand,'   │ Alcance:', alcc ,'║ ║')
    print('║ ╟──────────────┴──────────────╢ ║')
    print('║ ║          Tipo: ' + clss +  '          ║ ║')
    print('║ ╟─────────────────────────────╢ ║')
    print('║ ║        Encantamentos        ║ ║')
    print('║ ║ ' + enc1[e1] + '       ║ ║')
    print('║ ║ ' + enc2 + '     ║ ║')
    print('║ ║ ' + enc3 + '     ║ ║')
    print('║ ╚═════════════════════════════╝ ║')

    # Discord
    if dscd == 1:
      print('          Discode:\n')
      print(':a: = (' + dano + ') | :boom: = (' + crit + ') | :boomerang: = ' + alcc + ' | :gloves: = ' + hand)
      print('> - ' + rrdd[r] + ' ' + arma)
      if m != 0:
        print('> ||└ _ornado com_ ' + mtrl[m] + '||')
      if r >= 4:
        print('> ||└ _'+ enc1[e1] +'_||')
      if r >= 5:
        print('> ||└ _'+ enc2 +'_||')
      if r >= 6:
        print('> ||└ _'+ enc3 +'_||')

  # Print - Itens
  if ctgr >= 17 and ctgr <= 19:
    print('║ ╔═════════════════════════════╗ ║')
    print('║ ║            Ficha            ║ ║')
    print('║ ║ Item:                  ',rrdd[r],'║ ║')
    if ctgr == 17 or ctgr == 18:
      print('║ ║ >', item + '                    ║ ║')
    elif ctgr == 19:
      print('║ ║ >', item + '                  ║ ║')
    if m != 0:
      print('║ ║   └ ornado com', mtrl[m], '     ║ ║')
    else:
      print('║ ║   └ ∙∙∙                     ║ ║')    
    print('║ ╟─────────────────────────────╢ ║')
    print('║ ║           TIER:', tier,'          ║ ║')
    print('║ ╟──────────────┬──────────────╢ ║')
    print('║ ║ Defesa _ │+│ │ Defesa _ │+│ ║ ║')
    print('║ ║ Física ¯ │' + dffs + '│ │ Mágica ¯ │' + dfmg + '│ ║ ║')
    print('║ ╟──────────────┴──────────────╢ ║')
    print('║ ║      Resistência = ' + rstc + '      ║ ║')
    print('║ ╟─────────────────────────────╢ ║')
    print('║ ║        Encantamentos        ║ ║')
    print('║ ║ ' + enc1[e1] + '       ║ ║')
    print('║ ║ ' + enc2 + '     ║ ║')
    print('║ ║ ' + enc3 + '     ║ ║')
    print('║ ╚═════════════════════════════╝ ║')

    # Discord
    if dscd == 1:
      print('          Discode:\n')
      if item == 'Escudo':
        print(':b: :shield: = [+' + dffs + ']')
        print('> - ' + rrdd[r] + ' Escudo T' + str(tier))
      elif item == 'Adorno':
        print(':b: :gem: = [+' + dfmg + ']')
        print('> - ' + rrdd[r] + ' Adorno T' + str(tier))
      elif item == 'Armadura':
        print(':vs: :shield: = [+' + dffs + ']')
        print(':vs: :gem: = [+' + dfmg + ']')
        print('> - ' + rrdd[r] + ' Armadura T' + str(tier))
      if m != 0:
        print('> ||└ _ornado com_ ' + mtrl[m] + '||')
      if r >= 4:
        print('> ||└ _'+ enc1[e1] +'_||')
      if r >= 5:
        print('> ||└ _'+ enc2 +'_||')
      if r >= 6:
        print('> ||└ _'+ enc3 +'_||')