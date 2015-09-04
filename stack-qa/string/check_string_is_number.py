
print '12345'.isdigit()

a = '12345.6'

try:
    num = float(a)
    print 'str: 12345.6 contains only digits'
except:
    print "str: 12345.6 doesn't contains only digits"
