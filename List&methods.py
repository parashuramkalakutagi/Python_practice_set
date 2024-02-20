

# list comprehension
l1 = [i for i in range(20)]
print(l1)

# list comprehension method 2
l2 = [i for i in range(2,20,2)]
print(l2)

# list comprehension method with if else statement
l3  =  ['odd' if i%2==0 else 'even'  for i in range(1,11) ]
print(l3)

# list method append
l4 = []
l4.append('hello')
print(l4)


# list method sort arrange the list values in ascending order
l5 = ['hi' , 'hello', 'namaskara','apple','banana','cherry']
l5.sort()
print(l5)

# list index method return the index number of the item or value
print(l5.index('hi'))


# insert method use to add the element in list for specific index
l5.insert(0,'mango')
print(l5)

# Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits[0:1] = ['guava', 'banana','apple']
print(fruits)

for fruit in fruits:
    print(fruit,end=" ")

for fruit in fruits:
    if 'banana' in fruit:
        print(f' here we found your fruit : {fruit}')


squered_num = [x**2 for x in range(20)]
print(squered_num)