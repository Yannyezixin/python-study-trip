

# fast and can be used in 'str' and 'unicode' but UserString
def is_a_string(anobj):
    return isinstance(anobj, basestring)

# worst, can not be used once
def isExactlyAString(anobj):
    return type(anobj) is type('')

# all str can be check, include Userstring
def isStringLike(anobj):
    # more detail
    #try: anobj.lower( ) + ''
    try: anobj + ''
    except: return False
    else: return True


print is_a_string('abc')
print is_a_string(1123123)
print isExactlyAString('abc')
print isExactlyAString(123123)
print isStringLike('abc')
print isStringLike(12123)

