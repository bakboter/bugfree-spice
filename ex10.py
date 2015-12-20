# \t in text is tabbeed in 1 
tabby_cat = "\tI'm tabbed in."
#\ splits centesces in new lines 
persian_cat = "i'm split\non a line."
# doesn doe it with dobbel \\ removes one 
backslash_cat = "ii'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/", "-" ,"\\" ,"|" ,"i"]:
		print "%s\r" % i,
"""

"""