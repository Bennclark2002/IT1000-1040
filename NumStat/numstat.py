def stats(filename):
    try:
        f = open(file_name, 'r')

        nums = f.readlines()
        nums = [int(i) for i in nums]

        print("File name ; ",file_name)
        print("Sum: ",sum(nums))
        print("Count: ",len(nums) )
        print("Average:" , (sum(nums) / len(nums) ))
        print("Maximum;",max(nums))
        print("Minimum:",min(nums))
        print("Range : "+str(min(nums)) + " to " + str(max(nums)))

    except:
        print("An exception occurred : Enter a valid file name")


file_name = input("Enter file name : ")

while True:
    stats(file_name)
    next_op = input("Would you like to evaluate another file? (y/n) : ")
    if next_op == 'n':
        break
