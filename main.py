from itertools import product
Colin1 = list(product(range(1,7), repeat=6))
Peter1 = list(product(range(1,5), repeat=9))
Colin = map(lambda x: sum(x),Colin1)
Peter = map(lambda x: sum(x),Peter1)
k = {0:0,"1":0,"2":0,'3':0,'4':0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,3:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,34:0,35:0,36:0,37:0}
for i in list(Colin):
  for g in range(0,37):
    gg = str(g)
    if i == g:
      k.update(gg = 4)
    else: continue



PeterWin = 0
ColinWin = 0
Tie = 0
def runit():
  Colin1 = list(product(range(1,7), repeat=6))
  Peter1 = list(product(range(1,5), repeat=9))
  Colin = list(map(lambda x: sum(x),Colin1))
  Peter = map(lambda x: sum(x),Peter1)
  PeterWin = 0
  ColinWin = 0
  Tie = 0
  for pp in list(Peter):
    print("pp", pp)
    for y in Colin:
      if pp > y:
        PeterWin += 1
      else:
        ColinWin += 1
  print(PeterWin)
  print(ColinWin)
 
runit()
