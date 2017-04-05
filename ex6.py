# assign the string
# "There are 10 types of people."
# (the "10" is inserted via a format string formatter)
# to a variable called 'x'
x = "There are %d types of people." % 10

# assign the string
# "binary" to a variable called "binary"
binary = "binary"

# assign the string
# "don't" to a variable called "do_not"
do_not = "don't"

# assign the string
# "Those who know binary and those who don't."
# (where "binary" and "don't" are inserted via
# string formatters from the variables called
# "binary" and "do_not")
# to a variable called 'y'
y = "Those who know %s and those who %s." % (binary, do_not)

# print the string
# "There are 10 types of people."
# which was assigned to the variable called 'x' before
print x

# print the string
# "Those who know binary and those who don't."
# which was assigned to the variable called 'y' before
print y

# print "I said: 'There are 10 types of people.'"
# where the single-quoted string is inserted via a string formatter
# from the variable x
# the single quotes seem to be automatically inserted because
# x is "converted" into a string
print "I said: %r." % x

# print "I also said 'Those who know binary and those who don't.'."
# where the single-quoted string is inserted via a string formatter
# from the variable y
# the single quotes are part of the format string so they are not
# automatically inserted like before, although y is also "converted"
# to a string
print "I also said: '%s'" % y

# assign the boolean value False to a variable called "hilarious"
hilarious = False

# assign the format string "Isn't that joke so funny?! %r"
# to a variable called "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! %r"

# print the string that is the result of inserting the variable "hilarious"
# into the format string assigned to the variable called "joke_evaluation"
print joke_evaluation % hilarious

# assign the string "This is the left side of ..."
# to a variable called 'w'
w = "This is the left side of ..."

# assign the string "a string with a right side."
# to a variable called 'e'
e = "a string with a right side."

# print the result of concatenating the variabled 'w' and 'e'
print w + e
