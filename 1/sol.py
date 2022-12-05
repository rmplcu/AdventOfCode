def sol():
  lines = []
  with open('data.txt', 'r') as file:
    lines = [y.replace('\n', '') for y in file.readlines()]

  indexes = [i for i, v in enumerate(lines, 1) if v == '']
  elves = [sum(map(int, x[:-1])) for x in [lines[i:j] for i, j in zip([0]+indexes, indexes)]]
  
  t = []
  for x in range(3):
    t.append(elves.pop(elves.index(max(elves))))

  print(sum(t))


if __name__ == '__main__':
  sol()