score = input('Enter a score between 0.0 and 1.0:')
grade = 0
try:
    f_score = float(score)
    if f_score>=0.9:
        grade = 'A'
    elif f_score>=0.8:
        grade = 'B'
    elif f_score>=0.7:
        grade = 'C'
    elif f_score>=0.6:
        grade = 'D'
    elif f_score<0.6:
        grade = 'F'
    print(grade)
except:
    print('Score must be within 0.0 and 1.0!')
input('Press Enter to Quit')
