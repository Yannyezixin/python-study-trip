
listone = [1, 2, 3]
listtwo = [1, 4, 5]
listthree = [1, 2, 3]

# not consider sort
print listone + listtwo
listone.extend(listtwo) # it will change listone
print listone

# consider sort
print list(__import__('itertools').chain(listthree, listtwo))
