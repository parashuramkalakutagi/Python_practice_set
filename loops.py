

# wait with attempts
import time

max_attempt = 5
attempt = 0
wait_time = 1

while attempt < max_attempt:
    print('attempt : ',attempt+1,'wait-time :',wait_time)
    time.sleep(wait_time)
    attempt+=1
    wait_time*=2



#  1 question :: count positive numbers

numbers = [1,2,-3,-4,-5,6,7,-8,-9,10,11,12,13]
positive_num_count = 0

for num in numbers:
    if num > 0:
        positive_num_count+=1

print(f'Final Count : {positive_num_count}')


#  2 question :: calculate sum of even numbers up to n

number = [1,2,3,4,5,6,7,8,9,10]
sum_of_even_numbers = 0

for num in number:
    if num %2==0:
        sum_of_even_numbers+=num
print(sum_of_even_numbers)


# 3 question ::  print the table multiplication up to 10 , but skip the fifth itretion

num = 3

for i in range(1,11):
    if i == 5:
        continue
    print(f'3 X {i} = {i*num}')

# Reverse the string using loop

name = 'parashuram'
reversed_srting = ""
for i in name:
    reversed_srting = i + reversed_srting

print(reversed_srting)



# find the non repited character

string = 'teeter'
for char in string:
    if string.count(char) == 1:
        print(f'we found non repeted char :: {char}')


# keep asking number to user until they enter the number 1 and 10

while True:
    inp = int(input("Enter num b/w 1 to 10 :: >> "))
    if inp >= 1 and inp <=10:
        print(inp)
        break



# List Uniqueness Checker
list =  ['apple','banana','mango','mango','cherry','cherry']
unique_list = []
for val in list:
    if not val in unique_list:
        unique_list.append(val)
    else:
        print(val)
print(unique_list)




# Prime Number checker

while True:
    inp = int(input("Enter the number :: "))
    if inp%2==0:
        print('non-prime number :',inp)
    else:
        print('Prime number :: ',inp)


