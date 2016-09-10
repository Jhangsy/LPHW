# if you put functions in a base class
# then all subclasses will automatically get those features.
class Parent(object):

    def implicit(self):
        print "Parent implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# overiide
class Parent(object):

    def override(self):
        print "Parent override()"

class Child(Parent):
    def override(self):
        print "Child override()"


dad = Parent()
son = Child()

dad.override()
son.override()

# Super

class Parent(object):

    def altered(self):
        print "Parent altered()"

class Child(Parent):
    def altered(self):
        print "Child, before Parent altered()"
 # call super function with arguments Child&self then call altered() on whatever it returns
        super(Child, self).altered()
        print "Child, after Parent altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

class Other(object):

    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, before Ohter altered()"
        super(Child, self).altered()
        print "Child, after other altered()"

son = Child()

son.implicit()
son.override()
son.altered()
