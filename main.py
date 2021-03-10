from random import randint
import upgrade as u
import weapon as w
import spell as s
import ingot as i
import drink as d
import bag as b

wh = 0
print('╔═════════════════════════════════╗')
while wh < 3:
  r = randint(1, 100)
  if r >= 82:   # 19% 
    b.bag()
    wh = wh + 1
  elif r >= 64: # 18% 
    d.drink()
    wh = wh + 1
  elif r >= 47: # 17%
    i.ingot()
    wh = wh + 1
  elif r >= 31: # 16% 
    w.weapon()
    wh = wh + 1
  elif r >= 16: # 15%
    s.spell()
    wh = wh + 1
  elif r >= 2: # 14%
    u.up()
    wh = wh + 1
  else:        # 01%
    wh = wh - 1
print('╚═════════════════════════════════╝')
