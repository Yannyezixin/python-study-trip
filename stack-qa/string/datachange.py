import ast

a = "543.222"

print float(a)
print (int(float(a)))


print ast.literal_eval(a)
