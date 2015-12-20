#this ome is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print"arg1: %r, arg2: %r" % (arg1, arg2)
	
# oke, that *args is actly pointless, we can do this 
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#this just take one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
#this takes bo arguments
def print_none():
	print "i got nothing'."
	
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
