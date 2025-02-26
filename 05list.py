# Collection data type 
# Empty list
lst=[]
lst=list()
        # 0          1        2       3
fruit=['orange','banana','pawpaw','mango']
        # -4      -3       -2        -1
print(fruit)
print(len(fruit))

# Indexing
print(fruit[0])
# Negative Indexing
print(fruit[-4])

# Unpacking

box=['T-shirts','Trousers','socks','brush','suits','cream']
a,b,c,*rest=box

print(a+' '+b,rest)
print(box[3:4])
box[0]='kiwi'
print(box)
box.append('guava')
print(box)
box.insert(2,'corn')
print(box)
box.remove('guava')
print(box)
box.pop(4)
print(box)

print(fruit+box)

# del fruit

# print(fruit)
lst=box.copy()
box.clear()
print(box)
print(lst)
print(lst[::-1])
print(lst.reverse())
print(lst.sort())
print(lst.sort(reverse=True))