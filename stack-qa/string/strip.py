
s = " \t a string example \t  "

print s.strip() + '!'
print s.rstrip() + '!'
print s.lstrip() + '!'
print s.strip(' \t\n\ra') + '!'
print s.strip(' \ta') + '!'
