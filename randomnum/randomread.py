filename='randomnum.txt'

total_sum=0
count=0
with open(filename,'r') as infile:
    for line in infile.readlines():
        number = int(line.strip())
        count+=1
        total_sum+=number
        print(number)
print('Total Sum: {}' .format(total_sum))
print('Total numbers read: {}'.format(count))
