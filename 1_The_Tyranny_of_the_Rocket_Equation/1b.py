def findFirstRepeatedFreq(freqs):
	freqs = set([0])
	freq = 0

	while True:
		for line in lines:
		try:
			freq += int(line)
			if freq in freqs:
				print(freq)
				return
			else :
				freqs.add(freq) 
		except ValueError:
			print('Invalid input  %s' % line)

lines = []
with open('1_input.txt','r') as f:
	lines = f.readlines()

findFirstRepeatedFreq(lines)