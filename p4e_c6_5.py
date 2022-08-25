text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(':')
num_colon = text[colon+1:]
num_str = num_colon.lstrip()
num = float(num_str)
print(num)
input('Press Enter to Quit')
