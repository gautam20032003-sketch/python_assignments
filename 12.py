list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
unique = []
for i in list_with_duplicates:
    if i not in unique:
        unique.append(i)
print(unique)
