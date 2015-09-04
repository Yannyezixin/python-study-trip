def f(x):
    return {
        'a': out('a'),
        'b': 2,
    }.get(x, 9)

def out(x):
    print 'This is what you pass in:', x
