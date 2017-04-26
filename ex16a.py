from sys import argv

script, file_name = argv

print "You have chosen to open %s" % file_name
print "Opening ..."
file = open(file_name, 'r')
print "Reading ..."
lines = file.read()
print "Printing ...\n"
print lines
print "Closing %s ..." % file_name
file.close()
