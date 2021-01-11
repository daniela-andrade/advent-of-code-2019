import itertools
import queue
import threading

def getSeqs(rangeMin, rangeMax):
	return list(itertools.permutations([i for i in range(rangeMin, rangeMax)]))

def parseInst(inst, inputQueue, outputQueue, feedback, pointer=0):
	while True:
		if inst[pointer] == 99:
			break
		opcode = inst[pointer] % 10
		firstPositionMode = int(inst[pointer]/100) % 10
		lastPositionMode = int(inst[pointer]/1000) % 10

		if opcode != 3 and opcode != 4:
			valueOne = inst[inst[pointer+1]] if firstPositionMode == 0 else inst[pointer+1]
			valueTwo = inst[inst[pointer+2]] if lastPositionMode == 0 else inst[pointer+2]
			
			if opcode == 1:
				inst[inst[pointer+3]] = valueOne + valueTwo
			elif opcode == 2:
				inst[inst[pointer+3]] = valueOne * valueTwo
			elif opcode == 7:
				inst[inst[pointer+3]] = 1 if valueOne < valueTwo else 0
			elif opcode == 8:
				inst[inst[pointer+3]] = 1 if valueOne == valueTwo else 0	
			pointer += 4
			if opcode == 5 or opcode == 6:
				pointer = valueTwo if (valueOne != 0 if opcode == 5 else valueOne == 0) else pointer - 1
		else:
			if opcode == 3:
				while (True):
					if not inputQueue.empty():
						inst[inst[pointer+1]] = inputQueue.get()
						break
			if opcode == 4:
				while (True):
					if not outputQueue.full():
						outputQueue.put(inst[inst[pointer+1]])
					if not feedback:
						return
					break
			pointer += 2

def getMaxThruster(inst, initialSignal, minPhaseSetting, maxPhaseSetting, feedback=False):
	QUEUE_SIZE = 5
	maxOutput = 0
	numAmplifiers = maxPhaseSetting - minPhaseSetting + 1
	phaseSettings = getSeqs(minPhaseSetting, maxPhaseSetting + 1)

	for phase in range(len(phaseSettings)):
		print('Progress: %d %s' % (phase/len(phaseSettings)*100, '%'))
		threads = []
		inputQueue = queue.Queue(QUEUE_SIZE)
		firstQueue = inputQueue
		
		for amp in range(numAmplifiers):
			outputQueue = firstQueue if amp == numAmplifiers - 1 else queue.Queue(QUEUE_SIZE)
			inputQueue.put(phaseSettings[phase][amp])
			if amp == 0:
				inputQueue.put(initialSignal)
			kwargs = dict(inst=inst.copy(), inputQueue=inputQueue, outputQueue=outputQueue, feedback=feedback)
			threads.append(threading.Thread(target=parseInst, kwargs=kwargs))
			inputQueue = outputQueue

		for t in threads:
			t.start()
		for t in threads:
			t.join()

		maxOutput = max(maxOutput, firstQueue.get())
	return maxOutput
	
inst = []
with open('input.txt', 'r') as f:
	inst = [int(i) for i in f.readlines()[0].split(',')]

print('Final MAX_OUTPUT 1: %d' % getMaxThruster(inst, 0, 0, 4))
print('Final MAX_OUTPUT 2: %d' % getMaxThruster(inst, 0, 5, 9, True))