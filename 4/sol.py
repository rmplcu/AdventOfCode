def sol1(lines: list[str]):
  res = 0
  for x in lines:
    if x[0][0] in range(x[1][0], x[1][1]+1) and  x[0][1] in range(x[1][0], x[1][1]+1): res += 1
    elif x[1][0] in range(x[0][0], x[0][1]+1) and  x[1][1] in range(x[0][0], x[0][1]+1): res += 1

  print(res)

def sol2(lines: list[str], log=False):
  res = 0
  for x in lines:
    if (x[0][0] >= x[1][0] and x[0][0] <= x[1][1]) or (x[0][1] >= x[1][0] and x[0][1] <= x[1][1]) or (x[1][0] >=x[0][0] and x[1][0] <= x[0][1]) or (x[1][1] >= x[0][0] and x[1][1] <= x[0][1]):
      if log: print(x)
      res+=1

  print(res)
    

if __name__ == '__main__':
  lines = []
  with open('input.txt', 'r') as file:
    lines = [[list(map(int, x.split('-'))) for x in y.strip().split(',')] for y in file.readlines()]

  sol1(lines)
  sol2(lines)