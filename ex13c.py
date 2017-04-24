# combine raw_input with argv

from sys import argv

script_name = argv[0]

print "I am %s and these are my arguments!" % script_name
for a in argv[1:]:
    print a

user_name = raw_input("And what's your name? ")
print "I bet that isn't even your real name!"
print "So long, '%s'!" % user_name
