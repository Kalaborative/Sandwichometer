from random import choice

values = [True, False]

val1 = False
val2 = False

while not val1 and not val2:
	val1 = choice(values)
	val2 = choice(values)
	print "Value one: " + str(val1)
	print "Value two: " + str(val2)
