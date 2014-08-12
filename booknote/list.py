#list like C's array, but something different,it can store diff
#dataType.

#----------------------------------------------
#get part of list
list_name = ['a','b','c']
print list_name;

part_of_list_name = list_name[0:2]
print part_of_list_name

single = list_name[0]
print single

#use .index(item) to find a item's index
b = list_name.index('b')
print b

#use .insert(index, item) to insert a item including
list_name.insert(2,"I'm insert")
insert = list_name[2]
print insert
print "after insert:", list_name

#use .pop to remove something from list and it will return the item
#which was removed
remove = list_name.pop(2)
print "remove: %s" % (remove)
print "after remove: ",list_name

#----------------------------------------------------
#Strings as a list

animals = "catdogduck"

print animals[:3]
print animals[3:6]
print animals[6:]

#----------------------------------------------------
#For loop with lists

loop_list = [3,6,1,4,5,2]

for num in loop_list:
    print num

#use .sort() to sort a list, ps: it not return a new list
print "init loop_list", loop_list
loop_list.sort()
print "sorted list", loop_list

#use .append() to append a item into list
square_list = []
for num in loop_list:
    n = loop_list[num-1]
    square_list.append(n**2)
print "square_list use append:", square_list

