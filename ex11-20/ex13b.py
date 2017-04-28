# write a script that takes more (than three) arguments

from sys import argv

script_name = argv[0]

print "This is a script named", script_name
print "Look at all the meaningful data!"

for a in argv[1:]:
    print a
