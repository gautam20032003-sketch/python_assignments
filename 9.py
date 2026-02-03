# Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
a=[10,20,30]
b=a[:] #create a copy of list a
b.append(40) #modify the copied list
print("b",b)
print("a",a)