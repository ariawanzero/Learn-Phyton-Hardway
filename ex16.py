from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
raw_input("?")
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"

print "Now I'm going to ask you for three lines."

print "I'm going to write these to file."

target.write(raw_input("line 1: "))
target.write("\n")
target.write(raw_input("line 2: "))
target.write("\n")
target.write(raw_input("line 3: "))
target.write("\n")

print "And finally, we close it"
target.close()
