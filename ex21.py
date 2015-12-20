def add(a, b):
	print "adding %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "subtract %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print"devide %d / %d" % (a, b)
	return a / b 
	
	
print " lets do some math's with just functions "

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print " age % d Heught %d wieght %d iq %d " % (age, height, weight ,iq)

# a puzzel the extra cred it 

print "here is a puzzel."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "that becomes watt", what, ": can you do it by hand ?"