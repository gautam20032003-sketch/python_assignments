sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary","city"]
newdict={}
for i in keys:
    newdict[i]=sample_dict[i]
print(newdict)    
