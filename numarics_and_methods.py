


x = 15
y = 20

print(((x+y)*2)/4)

print(x**20)

import math

z = 2
print(math.floor(z))


print(oct(z))
print(hex(z))
print(bin(z))

import random

list = ['hi','hello','pk']
ranom = random.choice(list)
print(ranom)


ran = random.randint(1,1000)

random.shuffle(list)
print(ran)

print(random.Random())
print(random.randbytes(3))
print(random.shuffle(list))
print(list)


dict = {
    'name':'pk',
    'address':'gudas'
}

keys = []
values = []

for key in dict:
    print(f'{key}  :: {dict[key]}')
    keys.append(key)
    values.append(dict[key])

print(keys)
print(values)