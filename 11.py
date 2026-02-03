# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1.remove("")
# list1.remove("")
# print(list1)

list1=["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if i=="":
        list1.remove(i)
print(list1)