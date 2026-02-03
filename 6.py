# Given a string, create a dictionary where keys are characters and values are their frequencies in the string
string1 = 'Jessa'
c={}
for ch in string1:
    if ch in c:
        c[ch]+=1
    else:
        c[ch]=1 
print(c)           