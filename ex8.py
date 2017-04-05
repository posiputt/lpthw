# assign the format string "%r %r %r %r" to a variable called formatter
formatter = "%r %r %r %r"

# print "1 2 3 4" where the numbers are inserted into the format string
# called formatters
print formatter % (1, 2, 3, 4)

# print "'one' 'two' 'three' 'four'" (inserted into formatter)
print formatter % ("one", "two", "three", "four")

# print "True False False True" (inserted into formatter)
print formatter % (True, False, False, True)

# print '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# where the string literal formatter is inserted into the format string
# called formatter
print formatter % (formatter, formatter, formatter, formatter)

# print "'I had this thing' 'That you could type up right.'
# "But it didn't sing." 'So I said goodnight.'"
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
