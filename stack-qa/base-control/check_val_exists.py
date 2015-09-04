existsVal = 2

if 'myVal' not in locals():
    print 'myVal is not exists'

if 'existsVal' in locals():
    print 'existsVal is exists'

class obj():
    existsVal = 2

if hasattr(obj, 'existsVal'):
    print 'existsVal exists in obj'

if not hasattr(obj, 'myVal'):
    print 'myVal is not exists in obj'
