# String concatenation
firstname='John'
lastname='Precious'
space=" "
fullname=firstname+space+lastname
print(fullname)

# new line \n
print('The mana is going to \n the market')
# tab \t 
print('The man is going to the shop')
# back slash \\
print('The man is going to the \'mosque\'')
print("The man is going to the 'mosque'")

# String formating
# %s string
# %d  integer
# %.nf  floating point number  with fixed precision

first_name= 'John'
last_name='Paul'
language='Python'
age=2

formated_string='My name is %s %s,I am %d years old  and I love the %s programming language'%(firstname,last_name,age,language)

print(formated_string)

# New string formatting

formated_string=f'My name is {first_name} {last_name},I am {age} years old  and I love the {language} programming language'
print(formated_string)

# String Interpolation

formated_string=f'My name is {first_name} {last_name},I am {age+3} years old  and I love the {language} programming language'
print(formated_string)

a=5
b=6
sum=f'{a} + {b} = {a+b}'
print(sum)

language='My name is John Paul,I am 2 years old  and I love the Python programming language years'
# indexing
# print(language[0]+language[1]+language[2]+language[3])

# print(language[80])
print(language[10:34]) #slicing
print(language[::-1]) #reversing the string


# string methods
print(language.upper())
print(language.replace('Python','c#')) # replaces a substring
# print(language.split(,))# creates a new list
print(language.lower())
print(language.count('old',3,len(language)-1))
print(language.endswith('y'))
print(language.startswith('M'))
print(language.find('years')) # returns the first index of the occurrence
print(language.rfind('years')) # returns the last index of the occurrence
web_tech=['Html','css','Javascripts','React']
web_tech_str= ''.join(web_tech)
print(type(web_tech_str))


