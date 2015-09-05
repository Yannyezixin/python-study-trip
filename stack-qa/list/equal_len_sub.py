def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]



print list(chunks(range(1000), 10))
