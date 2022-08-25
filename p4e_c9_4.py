fname = input("Enter file name with extension:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)
mydict = dict()
for line in handle:
    if line.startswith('From '):
        words_list = line.split()
        #insert the name to the dictionary
        email = words_list[1]
        if email not in mydict:
            mydict[email] = 1
        else:
            mydict[email]=mydict[email]+1
max_key = max(mydict, key=mydict.get)
max_val = max(mydict.values())
print(max_key, max_val)
input('Press Enter to Quit')
