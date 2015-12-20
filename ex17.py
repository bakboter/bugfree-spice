from sys import argv
script, from_file, to_file = argv
in_file = open(from_file).read()
open(to_file, 'w').write(in_file)

""""
#from os.path import exists
#hoe kunnen deze regels 1 regel worden
# door de .read() van infile.read() aan de string infile = open fromfile.read() te maken

#in_data = in_file.read()

#print "Copying from %s to %s " % (from_file, to_file)
print ""the input file is %d bytes long "
does the outfile %r "
ready hit return to continue, ctrl-c to abort"
"" % (len(from_file), exists(to_file))
#raw_input()

#print "alright, all done "

#out_file.close()
#in_file.close()
"""