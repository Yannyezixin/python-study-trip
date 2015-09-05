
l = [range(3), range(3, 6), range(6, 10)]


# worst, like shit
new_list = [item for i in l for item in i]

# worse
new_list_2 = []
for i in l:
    new_list_2.extend(i)

print new_list
print new_list_2

