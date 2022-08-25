fname = input("Enter file name: ")
fh = open(fname)
num_counter = 0
num = 0
added = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colon_loc = line.find(':')
    num = line[(colon_loc+1):].strip()
    added = added + float(num)
    num_counter = num_counter + 1
avg_num = added/num_counter
print('Average spam confidence:', avg_num)
input('Press Enter to Quit')
