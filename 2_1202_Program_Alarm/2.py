codes = []
codesClone = []

def runCode(action, input1, input2, output):
	if codes[action] == 1:
		codes[codes[output]] = codes[codes[input1]] + codes[codes[input2]]
		return runCode(action+4, input1+4, input2+4, output+4)

	if codes[action] == 2:
		codes[codes[output]] = codes[codes[input1]] * codes[codes[input2]]
		return runCode(action+4, input1+4, input2+4, output+4)

	if codes[action] == 99:
		return codes[0]

with open('input.txt', 'r') as f:
	values = f.readlines()[0].split(',')
	codesClone = [int(i) for i in values]

#Challenge 1
codes = codesClone.copy()
codes[1] = 12
codes[2] = 2
print(runCode(0,1,2,3))

#Challenge 2
for i in range(0,100):
	for j in range(0,100):
		codes = codesClone.copy()
		codes[1] = i
		codes[2] = j
		if runCode(0,1,2,3) == 19690720:
			print(i, j)
			break