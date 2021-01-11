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

def parseInst(inst, inputQueue=[], outputQueue=[], feedback=False, pointer=0, base=0, extra=dict()):
	while True:

		val = getValue(pointer, inst, extra)
		if val == 99:
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
				addValue(getAddress(inst, pointer+1, firstPositionMode, base, extra), 2, inst, extra) 
			if opcode == 4:
				print(valueOne)
			if opcode == 9:
				base += valueOne
			pointer += 2
	
inst = []
with open('8_input.txt', 'r') as f:
	inst = [int(i) for i in f.readlines()[0].split(',')]

parseInst(inst)