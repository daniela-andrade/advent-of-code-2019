import sys

minCrossManhattan = sys.maxsize
minCrossLowestSteps = sys.maxsize

def updateCrossManhattan(x, y):
	global minCrossManhattan
	minCrossManhattan = min(minCrossManhattan, abs(x) + abs(y))

def updateCrossLowestSteps(x, y, grid, steps):
	global minCrossLowestSteps
	minCrossLowestSteps = min(minCrossLowestSteps, grid[(x,y)][1] + steps)

def addWireToGrid(wire, grid, addWireFunc, x=0, y=0, steps=-1):
	for dir in wire:
		if dir[0] == 'R':
			for r in range(x,x+int(dir[1:])):
				steps = addWireFunc(grid, r, y, steps)
			x += int(dir[1:])
		if dir[0] == 'U':
			for u in range(y,y+int(dir[1:])):
				steps = addWireFunc(grid, x, u, steps)
			y += int(dir[1:])
		if dir[0] == 'L':
			for l in range(x,x-int(dir[1:]),-1):
				steps = addWireFunc(grid, l, y, steps)
			x -= int(dir[1:])
		if dir[0] == 'D':
			for d in range(y,y-int(dir[1:]),-1):
				steps = addWireFunc(grid, x, d, steps)
			y -= int(dir[1:])

def addWireFuncOne(grid, x, y, steps):
	steps += 1
	grid[(x,y)] = (1, steps)
	return steps

def addWireFuncTwo(grid, x, y, steps):
	steps += 1
	if (x,y) in grid and grid[(x,y)][0] == 1:
		updateCrossManhattan(x,y)
		updateCrossLowestSteps(x,y,grid,steps)
		grid[(x,y)] = (3,steps)
	else:
		grid[(x,y)] = (2,steps)
	return steps

wireOne = []
wireTwo = []
with open('input.txt', 'r') as f:
	wireOne, wireTwo = [values.split(',') for values in f.readlines()]

grid = dict([])
addWireToGrid(wireOne, grid, addWireFuncOne)
grid[(0,0)] = (2,0)
addWireToGrid(wireTwo, grid, addWireFuncTwo)

print('MinCrossManhattan: %d' % minCrossManhattan)
print('MinCrossLowestSteps: %d' % minCrossLowestSteps)