def priority(x: str):
  if ord(x) <= ord('z') and ord(x) >= ord('a'):
    return ord(x) - ord('a') + 1

  if ord(x) <= ord('Z') and ord(x) >= ord('A'):
    return ord(x) - ord('A') + 27

  print("ERROR")
  return -1 
  

def sol1(lines: list[str]):
  res = []
  for x in lines:
    el1 = x[:int(len(x)/2)]
    el2 = x[int(len(x)/2):]

    res.append(sum(list(set([priority(y) for y in el1 if y in el2]))))
  
  print(sum(res))

def sol2(lines: list[str]):
  res = []
  for i in range(0, len(lines), 3):
    groups = lines[i:i+3]
    res.append(sum(list(set([priority(y) for y in groups[0] if y in groups[1] and y in groups[2]]))))

  print(sum(res))
    
  

if __name__ == '__main__':
  lines = []
  with open('input.txt', 'r') as f:
    lines = [y.strip() for y in f.readlines()]

  sol1(lines)
  sol2(lines)