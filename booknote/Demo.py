#String
Str = "MONTY"
StrIndex = "MONTY"[0]
StrLen = "String"

#get the length of string

length = len(StrLen)
print length

#get rid of all capitalization in string
print Str.lower()

#upper case
print StrLen.upper()

#str() turn non-string into strings
pi = 2.1
pi_str = str(pi)
pi_strType = type(pi_str)
print pi_str
print pi_strType

#link string, it must be same type

stringLink = Str + StrIndex + StrLen
print stringLink
print Str, 'xxxx'

# string Formattin with %

string_1 = "yann"
string_2 = "yezixin"
#better way
string_1_2 = " %s' chinese name is %s"%(string_1, string_2)
#not better way
string_1_2_two = string_1 + "'s chinese name is " + string_2
print string_1_2
print string_1_2_two

#-------------------------------------------------------
#Asking the user for input

#raw_input()

name = raw_input("what is your name?")

print "so your name is %s" % (name)
