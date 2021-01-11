import numpy

def getAddress(insts, pointer, positionMode, base, extra):
	if positionMode == 1:
		return pointer
	if positionMode == 2:
		return base + getValue(pointer, inst, extra)
	if positionMode == 0:
		return getValue(pointer, inst, extra)

def getValue(index, inst, extra):
	if len(inst) > index:
		return inst[index]
	elif index not in extra:
		extra[index] = 0
	return extra[index]

def addValue(index, value, inst, extra):
	if len(inst) > index:
		inst[index] = value
	else:
		extra[index] = value

def modifyPosition(val, pos, posX, posY):
	if val == 1:
		if pos == 'up':
			pos = 'right'
			posY += 1
		elif pos == 'right':
			pos = 'down'
			posX +=1
		elif pos == 'down':
			pos = 'left'
			posY -= 1
		elif pos == 'left':
			pos = 'up'
			posX -=1
	elif val == 0:
		if pos == 'up':
			pos = 'left'
			posY -= 1
		elif pos == 'right':
			pos = 'up'
			posX -=1
		elif pos == 'down':
			pos = 'right'
			posY += 1
		elif pos == 'left':
			pos = 'down'
			posX += 1
	return (posX, posY, pos)

def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

def parseInst(inst, inputQueue=[], outputQueue=[], feedback=False, pointer=0, base=0, extra=dict()):
	grid = numpy.ones( (6,45) )
	painted = []
	colorReceived = False
	posX = 0
	posY = 0
	pos = 'up'

	while True:

		val = getValue(pointer, inst, extra)
		if val == 99:
			print(len(painted))
			# grid[grid == 0] = ''
			# grid[grid == 1] = ' '
			for row in grid:
				line = ''
				for c in row:
					if c == 1:
						line += '#'
					else:
						line += ' '
				print(line)
			break

		opcode = val % 10
		firstPositionMode = int(val/100) % 10
		lastPositionMode = int(val/1000) % 10
		outputPositionMode = int(val/10000) % 10
		valueOne = getValue(getAddress(inst, pointer+1, firstPositionMode, base, extra), inst, extra)
		
		if opcode != 3 and opcode != 4 and opcode !=9:
			valueTwo = getValue(getAddress(inst, pointer+2, lastPositionMode, base, extra), inst, extra)
			outputAdress = getAddress(inst, pointer+3, outputPositionMode, base, extra)
			if opcode == 1:
				addValue(outputAdress, valueOne + valueTwo, inst, extra)
			elif opcode == 2:
				addValue(outputAdress, valueOne * valueTwo, inst, extra)
			elif opcode == 7:
				addValue(outputAdress, 1 if valueOne < valueTwo else 0, inst, extra) 
			elif opcode == 8:
				addValue(outputAdress, 1 if valueOne == valueTwo else 0, inst, extra) 
			pointer += 4
			if opcode == 5 or opcode == 6:
				pointer = valueTwo if (valueOne != 0 if opcode == 5 else valueOne == 0) else pointer - 1
		else:
			if opcode == 3:
				addValue(getAddress(inst, pointer+1, firstPositionMode, base, extra), grid[posX,posY], inst, extra) 
			if opcode == 4:
				if not colorReceived:
					grid[posX,posY] = valueOne
					colorReceived = True
					if (posX, posY) not in painted:
						painted.append((posX,posY))
				else:
					posX, posY, pos = modifyPosition(valueOne, pos, posX, posY)
					colorReceived = False
			if opcode == 9:
				base += valueOne
			pointer += 2
	
inst = []
with open('input.txt', 'r') as f:
	inst = [int(i) for i in f.readlines()[0].split(',')]

parseInst(inst)
