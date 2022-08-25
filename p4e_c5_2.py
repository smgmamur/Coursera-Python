user_list = []
while True:
    user_input = input('Enter an integer: ')
    if user_input != 'done':
        try:
            fl_ui = float(user_input)
            user_list.append(fl_ui)
        except:
            print('Invalid input')
    else:
        break
print('Maximum is',int(max(user_list)))
print('Minimum is',int(min(user_list)))
input('Press Enter to Quit')
