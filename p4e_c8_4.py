fname = input("Enter file name: ")
fh = open(fname)
mylist = list()
for line in fh:
    words = (line.rstrip()).split()
    for my_word in words:
        if my_word not in mylist:
            mylist.append(my_word)
mylist.sort()
print(mylist)
input('Press Enter to Quit')
