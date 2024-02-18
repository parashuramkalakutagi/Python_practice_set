names = ["Tony", "Natasha", "Thor", "Bruce","Tony",]
names.sort(reverse=True)
print(names)

print(names.count('Tony'))
print(names.sort(reverse=False))
new_list = names.copy()
print(new_list)
new_list.remove('Tony')
print(new_list)


items = [7, 4, 1, 0, 2, 5]
items.insert(1,90)
print(items)