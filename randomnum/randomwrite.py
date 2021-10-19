import random

count=int(input('How many random numbers do you want? '))
lower_bound=int(input('What is the lowest the random number should be: '))
upper_bound=int(input('What is the highest the random number should be: '))

filename='randomnum.txt'

with open(filename,'w') as outfile:
    for _ in range(count):
        random_number = random.randint(lower_bound,upper_bound)
        outfile.write('{}\n'.format(random_number))

print('The random numbers were written to {}'.format(filename))
