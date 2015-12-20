name = 'Benoit .G.A.R Prick'
age = 24 #echt waar
height = 184 # centimeter
wieght = 102 # KG
eyes = 'brown'
teeth = 'wit'
hair = "black"



# Metric to iprail conversion basic math's 
wieght_pounds = wieght * 2.20462262
heigh_inches = height * 0.393700787


print "let's talk about %s" % name
print "he's %d centimeter tall.'" % height
print "its a bit to heavy but stil healthy."
print " he's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usuaslly %s depending on the coffee." % teeth

print "so he way's in pounds %s"  % wieght_pounds
print "and is inches heigh %s" % heigh_inches
#this line is tricky, try to get it exactly right
print "If I add %d, and %d and %d and i get %r" % (
	age , height , wieght , age + height + wieght) 	
 
"""
my_name = 'Benoit .G.A.R Prick'
my_age = 24 #echt waar
my_height = 184 # centimeter
my_wieght = 102 # KG
my_eyes = 'brown'
my_teeth = 'wit'
my_hair = "black"

print "let's talk about %s" % my_name
print "he's %d centimeter tall.'" % my_height
print "its a bit to heavy but stil healthy."
print " he's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usuaslly %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, and %d and %d and i get %d" % (
	my_age , my_height , my_wieght , my_age + my_height + my_wieght) 	

	
let's talk about Benoit .G.A.R Prick
he's 184 centimeter tall.'
its a bit to heavy but stil healthy.
 he's got brown eyes and black hair.
His teeth are usuaslly wit depending on the coffee.
Traceback (most recent call last):
  File ".\ex5.py", line 16, in <module>
    print " If I add %d, and %d and %d i get %d" % (my_age ,my_height ,my_wieght ,my_age + my_height + my_wieght)
TypeError: not all arguments converted during string formatting

let's talk about Benoit .G.A.R Prick
he's 184 centimeter tall.'
its a bit to heavy but stil healthy.
 he's got brown eyes and black hair.
His teeth are usuaslly wit depending on the coffee.
Traceback (most recent call last):
  File ".\ex5.py", line 16, in <module>
    print " If I add %d, and %d and %d " % (my_age ,my_height ,my_wieght ,my_age + my_height + my_wieght)
TypeError: not all arguments converted during string formatting
fix 

print "If I add %d, and %d and %d and i get %d" % (
	my_age , my_height , my_wieght , my_age + my_height + my_wieght) 	
	
	
Study drils

1. 
haal my weg 

"""