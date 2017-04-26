from sys import argv
from os.path import exists

script, from_file, to_file = argv

# this is pretty ugly :)
open(to_file, 'w').write(open(from_file).read())
