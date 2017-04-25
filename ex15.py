# import the argv part of the sys module
from sys import argv

# assighn the script name to variable script
# and the first argument to variable filename
script, filename = argv

# assign the new file object from open to variable txt
# or maybe this is a better explanation:
# open the file, save it in variable txt
txt = open(filename)

# print the filename and some stuff
print "Here's your file %r" % filename
# print the contents of the file
print txt.read()
txt.close()

'''
# prompt for filename input
print "Type the filename again:"
# save the file name to file_again
file_again = raw_input("> ")

# open the new file and save to txt_again
txt_again = open(file_again)

# print the contents of the new file
print txt_again.read()
txt_again.close()
'''
