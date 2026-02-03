employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result={}
for i in employees:
    temp={}
    for k in defaults:
        temp[k]=defaults[k]
    result[i]=temp
print(result)