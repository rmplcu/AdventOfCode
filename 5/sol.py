def sol(stack: list[str], ops:list[int]):
  #initialize stacks
  stacks = [] 
  for i in range(len(stack[0])):
    stacks.append([])

  for x in stack:
    for i in range(len(x)):
      if x[i] != '-': stacks[i].append(x[i])

  #execute operations
  for x in ops:
    for i in range(x[0]):
      if not len(stacks[x[1]-1]) == 0:
        res = stacks[x[1]-1].pop()
        stacks[x[2]-1].append(res)

  #get top chars
  out = ""
  for x in stacks:
    out += x[-1]

  print(out)

def sol2(stack: list[str], ops:list[int]):
  #initialiize stack
  stacks = [] 
  for i in range(len(stack[0])):
    stacks.append([])

  for x in stack:
    for i in range(len(x)):
      if x[i] != '-': stacks[i].append(x[i])

  #execute operations
  for x in ops:
    partial = []
    for i in range(x[0]):
      if not len(stacks[x[1]-1]) == 0:
        res = stacks[x[1]-1].pop()
        partial.append(res)

    partial.reverse()
    stacks[x[2]-1] += partial      

  #get top chars
  out = ""
  for x in stacks:
    out += x[-1]

  print(out)


if __name__ == '__main__':
  lines = []
  with open('input.txt', 'r') as f:
    lines = [y.replace('\n', '') for y in f.readlines()]
  
  stacks = lines[:lines.index('')]
  stacks.reverse()
  stacks = [y.replace('[', '').replace(']', '').replace('    ', ' - ').replace(' ', '') for y in stacks[1:]]
  ops = [list(map(int, y.replace('move', '').replace('from', '').replace('to', '')[1:].replace('  ', ',').split(','))) for y in lines[lines.index('')+1:]]

  sol(stacks, ops)
  sol2(stacks, ops)