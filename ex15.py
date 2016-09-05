# exercise 15
from sys import argv # import argv

script, filename = argv # unpacking iniput

txt = open(filename) # open file

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
