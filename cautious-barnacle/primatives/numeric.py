import math

number = -41.2
lowerNumber = -300
higherNumber = 96

absoluteNumber = abs(number)
print absoluteNumber

ceilingNumber = math.ceil(number)
print ceilingNumber

floorNumber = math.floor(number)
print floorNumber

print min(number, lowerNumber)

print max(number, higherNumber)

powerNumber = number ** 2
alternatePowerNumber = math.pow(number, 2)

print powerNumber
print alternatePowerNumber

squareRootNumber = math.sqrt(higherNumber)
print(squareRootNumber)
