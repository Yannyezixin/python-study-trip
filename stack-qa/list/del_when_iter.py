oldlist = range(100)

newlist = [x for x in oldlist if x%2]
print newlist

# lose old quotation
oldlist = [x for x in oldlist if x%2]
print oldlist

# update at old list
oldlist[:] = [x for x in oldlist if x%2]
print oldlist

from itertools import ifilterfalse
oldlist[:] = list(ifilterfalse(lambda x: not x%2, range(100)))


print oldlist
