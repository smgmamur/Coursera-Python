filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
handle = open(filename)
mydict = dict()
newdict = dict()
for line in handle:
    if line.startswith("From "):
        word_list = line.split()
        hour = ((word_list[5]).split(':'))[0]
        if hour not in mydict:
            mydict[hour] = 1
        else:
            mydict[hour] = mydict[hour] + 1
keylist = list()
for k, v in mydict.items():
    keylist.append(k)
keylist.sort()
for key in keylist:
    val = mydict[key]
    print(key, val)

input("Press Enter to Quit")
