

dict = {
    'name':'pk',
    'address':'gudas',
    'pin':'591306'
}

for i in dict:
    print(f' key : {i}  ;; value:{dict[i]} ')


print(dict.keys())
print(dict.values())
print(dict.items())

for key , value in dict.items():
    print(f' {key} :: {value}')


# Create a dictionary with 3 keys, all with the value 0
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)




# Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

# set default value for specific key
cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
y = cars.setdefault("model", "Bronco")
print(y)


cars.pop('year')
print(cars)


# del keyword delete the key value of specific key
del cars['brand']
print(cars)


# squerd numbers test with dict and for loop

squerd_number = {x:x**2 for x in range(10)}
print(squerd_number)



