import re
import copy
import math

starts = []
with open('input.txt', 'r') as f:
	stars = f.readlines()

pos = []
pattern = re.compile(r'.*x=([-]?\d*).*y=([-]?\d*).*z=([-]?\d*)')
count = 0
for i in range(0, len(stars)):
	x, y, z = re.match(pattern, stars[i]).groups()
	values = [int(x), int(y), int(z), 0, 0, 0]
	pos.append(values)

def getUpdate(pos, i, j, index):
	update = 0
	if pos[i][index]  > pos[j][index]:
		update = -1
	elif pos[i][index]  < pos[j][index]:
		update = 1
	return update
	
def applyGravity(pos, index):
	for i in range(len(pos)):
		for j in range(len(pos)):
			if i != j:
				pos[i][index+3] += getUpdate(pos, i, j, index)
	return pos

def applyVelocity(pos, index):
	for i in range(len(pos)):
		pos[i][index] += pos[i][index+3]
	return pos

def getTotal(pos):
	total = 0
	for star in pos:
		potential = abs(star[0]) + abs(star[1]) + abs(star[2])
		kinetic = abs(star[3]) + abs(star[4]) + abs(star[5])
		total += potential * kinetic
	return total

def compareStates(one, two, col, rounds):
	for i in range(len(one)):
		if one[i][col] != two[i][col] or one[i][col+3] != two[i][col+3]:
			return 0
	return rounds

def getFinal(pos):
	def _lcm(a, b):
		return abs(a*b) // math.gcd(a, b)

	rounds = 0
	found = [0,0,0]
	posOriginal = copy.deepcopy(pos)
	while found[0]==0 or found[1]==0 or found[2]==0:
		rounds += 1
		print(rounds)
		for col in range(3):
			if found[col] == 0:
				pos = applyGravity(pos, col)
				pos = applyVelocity(pos, col)
				found[col] = compareStates(pos, posOriginal, col, rounds)
		print(rounds, found)
	print(found)

	print(_lcm(_lcm(found[0], found[1]), found[2]))

getFinal(pos)

