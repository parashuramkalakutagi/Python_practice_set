


list = [x for x in range(20) if x % 2 == 0]
# print(list)


# List comprehension with function

def multi(x):
    return x ** 2

l1 = [multi(x) for x in range(20)]
# print(l1)



l2 = [name for name in 'hanuman']
# print(l2)

nl = []
l3 = [x for x in range(20) if x % 2==0 ]
nl.append(l3)
# print(nl)


nl2 = []
list4 = ['even' if i%2==0 else 'odd' for i in range(10)]
nl2.append(list4)
for i,num in enumerate(nl2[0],start=0):
    print(f'{i}, {num}')



fruites = ['apple','banana','cherry','manago']
f2 = []
f2.append([fruite for fruite in fruites if 'a' in fruite])
print(f2[0])


fruites_2 = ['apple','banana','cherry','manago']

for fruite in fruites_2:
    if 'a' in fruite:
        f2.append(fruite)
    else:
        None
print(f2)