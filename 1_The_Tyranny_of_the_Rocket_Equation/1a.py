masses = []
with open('input.txt','r') as f:
	masses = f.readlines()

def getFuel(mass):
	return floor(mass/3) - 2

def getExtraFuel(mass):
	fuel = getFuel(mass)
	if fuel > 0:
		return fuel + getFuel(fuel)
	return 0

def getFirstLevelFuel(masses):
	return sum([getFuel(mass) for mass in masses])

def getTotalFuel(masses):
	return sum([getExtraFuel(mass) for mass in masses])

print('FUEL 1: %d' % getFirstLevelFuel(masses))
print('FUEL 2: %d' % getTotalFuel(masses))