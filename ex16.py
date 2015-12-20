#gets a module called argv
from sys import argv 

script, filename = argv 

print "we are going to erase %r ." % filename
print "if you dont want that hit ctrl +c (^c)."
print "if you do want that hit, return"

raw_input("?")

print "opning the file..."
target = open(filename, 'w')

print"Truncating the file. Goodbay!"
target.truncate()

print "now I'm going to ask you for three lines ."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "i'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()