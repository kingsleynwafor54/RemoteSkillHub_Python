empty_dict={}
empty_dict1=dict()
print(empty_dict)
print(empty_dict1)

# creating an empty collection
lst=list()
tp=tuple()
st=set()
dt=dict()

# Dictionary with values
dct={'key':'values','key1':'values'}

print(dct)

person={
  'first_name':'john',
  'last_name':'paul',
  'is_married':True,
  'skills':['HTML','CSS','JAVASCRIPT'],
  'address':{
    'street':'north-bank market',
    'zip_code':'111111'
  }
}

print(person)

print(len(person))

# accessing the values in a dictionary
print(person['address'])
print(person.get('address'))

print('address' in person)
print(person.keys())
print(person.items())
print(person.values())
