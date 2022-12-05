eq = {'A': 'S', 'B': 'C', 'C': 'F', 'X': 'S', 'Y': 'C', 'Z': 'F'}

def computeWin(x, y, log=False):
  p1 = eq[x]
  p2 = eq[y]
  value = ord(y) - ord('W')

  #draw
  if p1 == p2:
    if log: print(p1, p2, value+3)
    return value + 3

  #lose
  if (p1 == 'S' and p2 == 'F') or (p1 == 'F' and p2 == 'C') or (p1 == 'C' and p2 == 'S'):
    if log: print(p1, p2, value)
    return value

  #win
  if log: print(p1, p2, value+6)
  return value + 6

def sol(log = False):
  lines = []
  with open('input.txt', 'r') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]

  res = []
  for x in lines:
    res.append(computeWin(x[0], x[1], log))

  print(sum(res))

to_win = {'A':'B', 'B':'C', 'C':'A'}
to_lose = {'A':'C', 'B': 'A', 'C': 'B'}
values = {'A':1, 'B':2, 'C':3}
def sol2(log = False):
  lines = []
  with open('input.txt') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]

  res = []
  for x in lines:
    partial = 0
    if x[1] == 'X': #lose
      me = to_lose[x[0]]
      partial = values[me]
    elif x[1] == 'Y': #draw
      partial = values[x[0]] + 3
    else: #win
      me = to_win[x[0]]
      partial = values[me] + 6

    if log: print(x, partial)
    res.append(partial)

  print(sum(res))
      





if __name__ =='__main__':
  sol()
  sol2()

"""
Sasso -> 0 => 0, 1
Carta -> 1 => 1, 2
Forbice -> 2 => 2, 0

Strategy: 
  R -> P => 0,1 --> 8
  P -> R => 1,0 --> 1
  S -> S => 2,2 --> 6
"""