# imports argv module !

from sys import argv
# sets values for scips and filename for the argv module 
script, filename = argv 

# sets value for txt and opends the insterted filename 
txt = open(filename)
# prints text + filename 
print "Here's your file %r:" % filename
# prints text 
print txt.read()

# does the same as above only now asks for file name ,
# in program instead of add ing it to the terminal
print "Type the filename again:"

#asks for the file name in the program 
file_again = raw_input("> ")
# opens text and preps it for printing 
txt_again = open(file_again)
# prints text file 
#print txt_again.read()

