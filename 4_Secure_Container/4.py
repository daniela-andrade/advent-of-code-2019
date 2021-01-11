import math

def digit(digit, order):
	return int(digit/order) % 10
	
def digits(n, orders):
	return [digit(n, order) for order in orders]

def checkTwoAdjacent(digits, exactlyTwo):
	hasTwo = False
	if len(digits) < 2:
		return False
	if len(digits) == 2:
		return digits[0] == digits[1]
	for i in range (len(digits)-1):
		if i == 0:
			hasTwo = hasTwo  or (digits[i] == digits[i+1] and ((digits[i+1] != digits[i+2]) if exactlyTwo else True))
		elif i == len(digits)-2:
			hasTwo = hasTwo or (digits[-1] == digits[-2] and ((digits[-2] != digits[-3]) if exactlyTwo else True))
		else:
			hasTwo = hasTwo or (digits[i] == digits[i+1] and (((digits[i+1] != digits[i+2] and digits[i] != digits[i-1])) if exactlyTwo else True))
	return hasTwo
	
def checkIncreasing(digits):
	isIncreasing = True
	for digit in range (len(digits)-1):
		isIncreasing = isIncreasing and digits[digit] <= digits[digit+1]
	return isIncreasing

def getNumPasswords(rangeMin, rangeMax, restrictive):
	passwordCount = 0
	orders = [int(math.pow(10,power)) for power in range(len(str(rangeMax))-1,-1,-1)]
	for password in range(rangeMin,rangeMax):
		passwordDigits = digits(password, orders)
		if checkTwoAdjacent(passwordDigits, restrictive) and checkIncreasing(passwordDigits):
			passwordCount += 1
	return passwordCount

print('Password Count 1: %d' % getNumPasswords(183564,657474, False))
print('Password Count 2: %d' % getNumPasswords(183564,657474, True))