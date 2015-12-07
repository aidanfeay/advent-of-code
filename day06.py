grid = [[False for x in range(1000)] for x in range(1000)]
grid_2 = [[0 for x in range(1000)] for x in range(1000)]

print str(len(grid)) + " x " + str(len(grid[0]))

def update_grid(command, x1, y1, x2, y2):
  for x in range(x1, x2+1):
    for y in range(y1, y2+1):
      if command == 'turn on':
        grid[x][y] = True
      elif command == 'turn off':
        grid[x][y] = False
      elif command == 'toggle':
        grid[x][y] = True if grid[x][y] == False else grid[x][y] == False
      else:
        print 'not a valid instruction'

def update_grid_2(command, x1, y1, x2, y2):
  for x in range(x1, x2+1):
    for y in range(y1, y2+1):
      if command == 'turn on':
        grid_2[x][y] += 1
      elif command == 'turn off':
        if grid_2[x][y] > 0:
          grid_2[x][y] -= 1 
      elif command == 'toggle':
        grid_2[x][y] += 2
      else:
        print 'not a valid instruction'

with open('day06_input.txt') as instructions:
  for instruction in instructions:
    print instruction
    if 'turn on' in instruction:
      command = 'turn on'
    elif 'turn off' in instruction:
      command = 'turn off'
    elif 'toggle' in instruction:
      command = 'toggle'
    else:
      print 'not a valid instruction'
    coords = []
    for each in instruction.replace(',',' ').split():
      if each.isdigit():
        coords.append(int(each))
    update_grid(command,coords[0],coords[1],coords[2],coords[3])
    update_grid_2(command,coords[0],coords[1],coords[2],coords[3])

lit = 0
for x in range(1000):
  for y in range(1000):
    if grid[x][y]:
      lit += 1

print 'Part 1: ' + str(lit)

brightness = 0
for x in range(1000):
  for y in range(1000):
    brightness += grid_2[x][y]

print 'Part 2: ' + str(brightness)