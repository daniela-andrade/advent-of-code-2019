minCrossManhattan = 1000000
def updateCrossManhattan(x, y):
	global minCrossManhattan
	newCross = abs(x) + abs(y)
	if minCrossManhattan > newCross:
		minCrossManhattan = newCross

minCrossLowestSteps = 1000000
def updateCrossLowestSteps(x, y, stepsTwo):
	global minCrossLowestSteps
	newCross = grid[(x,y)][1] + stepsTwo
	if minCrossLowestSteps > newCross:
		minCrossLowestSteps = newCross

values = []
values2 = []
with open('input.txt', 'r') as f:
	lines = f.readlines()
	values = lines[0].split(',')
	values2 =lines[1].split(',')
grid = dict([])

x = 0
y = 0
steps = -1

for direction in values:	
if direction[0] == 'R':
	for r in range(x,x+int(direction[1:])):
		steps += 1
		grid[(r,y)] = (1, steps)
	x += int(direction[1:])
if direction[0] == 'U':
	for u in range(y,y+int(direction[1:])):
		steps += 1
		grid[(x,u)] = (1,steps)
	y += int(direction[1:])
if direction[0] == 'L':
	for l in range(x,x-int(direction[1:]),-1):
		steps += 1
		grid[(l,y)] = (1,steps)
	x -= int(direction[1:])
if direction[0] == 'D':
	for d in range(y,y-int(direction[1:]),-1):
		steps += 1
		grid[(x,d)] = (1,steps)
	y -= int(direction[1:])

x = 0
y = 0
steps = -1
grid[(0,0)] = (2,0)

for direction in values2:	
if direction[0] == 'R':
	for r in range(x,x+int(direction[1:])):
		steps += 1
		if (r,y) in grid and grid[(r,y)][0] == 1:
			updateCrossManhattan(r,y)
			updateCrossLowestSteps(r,y,steps)
			grid[(r,y)] = (3,steps)
		else:
			grid[(r,y)] = (2,steps)
	x += int(direction[1:])

if direction[0] == 'U':
	for u in range(y,y+int(direction[1:])):
		steps += 1
		if (x,u) in grid and grid[(x,u)][0] == 1:
			updateCrossManhattan(x,u)
			updateCrossLowestSteps(x,u,steps)
			grid[(x,u)] = (3,steps)
		else:
			grid[(x,u)] = (2,steps)
	y += int(direction[1:])

if direction[0] == 'L':
	for l in range(x,x-int(direction[1:]),-1):
		steps += 1
		if (l,y) in grid and grid[(l,y)][0] == 1:
			updateCrossManhattan(l,y)
			updateCrossLowestSteps(l,y,steps)
			grid[(l,y)] = (3,steps)
		else:
			grid[(l,y)] = (2,steps)
	x -= int(direction[1:])

if direction[0] == 'D':
	for d in range(y,y-int(direction[1:]),-1):
		steps += 1
		if (x,d) in grid and grid[(x,d)][0] == 1:
			updateCrossManhattan(x,d)
			updateCrossLowestSteps(x,d,steps)
			grid[(x,d)] = (3,steps)
		else:
			grid[(x,d)] = (2,steps)
	y -= int(direction[1:])


print(minCrossManhattan)
print(minCrossLowestSteps)