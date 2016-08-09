from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?

print "The input file is %d bytes long" % len(open(from_file).read())

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to Continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w').write(open(from_file).read())

print "Alright, all done."

