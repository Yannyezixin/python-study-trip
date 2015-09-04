import ast

s = "{'name': 'yann'}"

dic = ast.literal_eval(s)

print dic['name']


