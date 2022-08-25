import re
myfile = input('Enter file name: ')
if len(myfile) < 1:
    myfile = 'regex_sum_1558281.txt'
handle = open(myfile)
sum = 0
for line in handle:
    numlist = re.findall('[0-9]+', line)
    for num in numlist:
        num_int = int(num)
        sum = sum + num_int
print(sum)
input("Press Enter to close this window")
