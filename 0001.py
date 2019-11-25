#First problem 


#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

multiple_list = []

for val in range(1, 1000):
    if val%3==0 or val % 5 ==0:
        multiple_list.append(val)

result = sum(multiple_list)
print(result)
