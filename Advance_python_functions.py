

def all_sum_numbers(*args):
    return sum(args)

val = all_sum_numbers(1,2,3,4,5,6,7,8,9,10)
print(val)



def kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f'{key} : {value}')

print(kwargs(name='parashu',village='guadas',pincode=591306))



# using yield key-word yield keyword allow to itrate the function

def genrator(limit):
    for i in range(1,limit+1,2):
        yield i

for i in genrator(20):
    print(i)