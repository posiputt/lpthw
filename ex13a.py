# write a script that has fewer (than tree) arguments

from sys import argv

script_name, value1, value2 = argv

print "This is a script named", script_name
print "It takes two arguments. Their values now:", value1, value2
