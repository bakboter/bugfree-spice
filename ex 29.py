people = 20 
cats = 30 
dogs = 15 
"""
Deze eerste 3 regels geven aan wat de waardese zijn van people , cats ,dogs

"""
if people < cats:
	
	print " too manny cats ! the world is doomded ! "
#de if statement test of de statement clopt zo ja excute 
if people >= cats:
	print "not many cats! The world is saved!"
if people < dogs:
	print "the world is drooled on!"
if people > dogs:
	print "the world is dry"
	
	
dogs += 5 

if people >= dogs:
	print "people are greater than or eqaul to dogs"

if people <= dogs:
	print " People are lees than or eqeal to dogs."
	
if people == dogs:
	print "people are dogs"

"""

    What do you think the if does to the code under it?
	Excute if the "if" statment is treu 
    Why does the code under the if need to be indented four spaces?
	Or a tab this lets python know its part ofthe If statement above
    What happens if it isn't indented?
	IndentationError: expected an indented block
    Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
    What happens if you change the initial values for people, cats, and dogs?

"""