#imports the argv script
from sys import argv

# definse script and input_file that is given in the terminal.

script, input_file = argv
# prints the document 
def print_all(f):
	print f.read()
	
def rewind(f):
	print f.seek(0)
	
def print_a_line(line_count, f):
		print line_count,f.readline()
		
current_file = open(input_file)

print "first let's print the whole file:\n'"

print_all(current_file)

print "now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)