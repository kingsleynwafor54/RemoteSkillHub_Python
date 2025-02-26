language='The boys are getting ready for their python test'
a,b,c,d,*rest=language
print(f'{a}--{b}--{c}--{d}--{rest}')



lst=[1,2,3,4,5,6,7,8,9]
tp=(1,2,3,4,5,6,7,8,9)
tp=(1,2,3,4,5,6,7,8,9)
lst[1]=99
tp=list(tp)# converting  a tuple to a list
tp[1]=99# reassigning the index
tp=tuple(tp)# converting the list back to a tuple
print(tp)
tp1=(2,4,6,8,10) # creating an empty tuple
print(tp[:3])#slicing
print(tp+tp1)


