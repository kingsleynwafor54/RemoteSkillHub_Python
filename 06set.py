# creating a set
st=set()
print(type(st))

st1={}
print(type(st1))

# creating set with items
st1={'banana','mango','banana'}
print(st1)

# getting the total number of elements in a set
print(len(st1))

# adding items to a set 
st1.add('kiwi')
print(st1)

#To add multiple elements into a set
updated_set_items=['guava','orange','carrot']
st1.update(updated_set_items)

print(st1)

# removing elements from a set 
for i in updated_set_items:
  st1.remove(i)
print(st1)
st1.clear()
print(st1)
# del st1
# print(st1)