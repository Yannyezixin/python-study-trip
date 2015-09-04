class foo(object):
    def __eq__(self, other):
        return True

f = foo()
f2 = foo()
print "f == None: ", f == None
print "f == f2: ", f == f2
print "f is None: ", f is None
print "f is f2: ", f is f2
print "id(f) == id(f2): ", id(f) == id(f2)


