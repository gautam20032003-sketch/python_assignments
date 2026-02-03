my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession':'docter'}
my_dict.pop('profession')
print(my_dict)
for key,value in my_dict.items():
  print(f"{key}:{value}")
for i in my_dict:
  if i=="age":
   print("exist")  