#input to be given as a string with spaces
inp = [int(i) for i in input().split() if i.isdigit()]
peak = 0
temp_peak = 0
for i in range(len(inp)):
  if i %2 == 0:
    temp_peak += inp[i]
  if i %2 != 0:
    temp_peak -= inp[i]
  if temp_peak > peak:
    peak = temp_peak
y = peak+1
x = sum(inp)
arr = [[' ']*(x+2) for i in range(y+2)]
x = 0
for i in range(len(inp)):
  if i %2 == 0:
    for j in range(inp[i]):
      if y == 2:
        arr[y][x] = '<'
        arr[y-1][x] = '/'
        arr[y-1][x+1] = '|'
        arr[y-2][x+1] = 'o'
        arr[y-1][x+2] = '\\'
        x+=1
      if y>2:
        arr[y][x] = '/'
      if j != inp[i]-1:
        x += 1
        y -= 1
      else:
        x += 1
  if i %2 != 0:
    for j in range(inp[i]):
      if y == 2:
        arr[y][x] = '>'
      if y>2:
        arr[y][x] = '\\'
      if j != inp[i]-1:
        y += 1
        x += 1
      else:
        x += 1
for i in arr:
  for j in i:
    print(j, end="")
  print()
