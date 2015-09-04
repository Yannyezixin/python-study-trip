str = 'This is my name!'

if 'is' not in str:
    print 'is not found in the str'
else:
    print 'is found in the str'

if str.find('is') == -1:
    print 'is not found in the str by the method find'
else:
    print 'is found in the str by the mothod find'
