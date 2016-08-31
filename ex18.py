# Exerciese 18
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

#OK,  that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this one takes one arguments
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Jhang", "Yan")
print_two_again("Jhang", "Yan")
print_one("First!")
print_none()
