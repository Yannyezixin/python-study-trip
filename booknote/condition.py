x = 10

if x > 2:
    print "Large"

if x > 2:
    print 'a'
elif x > 10:
    print 'b'
else:
    print 'c'

#------errors and exception---------

num = 4

if num < 10:
    try:
        num = num ** 3
        num2 = num*3
        print num
        print num2x
    except:
        print "error"

#ask a integer or except a error
while True:
    try:
        num = int(raw_input("Enter an integer number:"))
        break
    except ValueError:
        print "This is not valid number!Try again..."
