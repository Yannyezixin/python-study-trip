import copy

class Foo(object):

    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


foo = Foo(1)

a = ['foo', foo]
b = a[:]
c = list(a)

# slow
d = copy.copy(a)

# slowest
e = copy.deepcopy(a)

foo.val = 5

print "a:", a
print "b:", b
print "c:", c
print "d:", d
print "e:", e
