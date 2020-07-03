class Other(object):

    def override(self):
        print("OTHER override()", self)

    def implicit(self):
        print("OTHER implicit()", self)

    def altered(self):
        print("OTHER altered()", self)

class Child(object):

    def __init__(self):
        self.other = Other()   # use this to get properties from other classes instead of inheritance

    def implicit(self):
        self.other.implicit()    # and then we can call methods/functions from other class

    def override(self):
        print("CHILD override()", self)

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()         # and the same thing for wrapper
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
print('-' * 20)
son.override()
print('-' * 20)
son.altered()
