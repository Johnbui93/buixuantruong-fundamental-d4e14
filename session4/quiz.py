import pyexcel
#from random

quizs = pyexcel.iget_records(file_name='quizx.xlsx')

for quiz in quizs:
    quiz['choice'] = quiz['choice'].split(',')
    print(quiz['question'])

# quizs = [{
#         'question': 'con nhen co may chan',
#         'choices': [3,4,5,6],
#         'right_choice': 3,
#     },
#     {
#         'question': 'con cho co may chan',
#         'choices': [3,4,5,6],
#         'right_choice': 1,
#     },
# ]
correct = 0
quizs = list(quizs)
for quiz in quizs:
    print(quiz['question'])
    for i in range(len(quiz['choices'])):
        print(f'{i+1}. {quiz["choices"][i]}')
    ans = int(input('your answer?'))-1
    if ans == quiz['right_choice']:
        print('you are correct')
        correct = correct +1
    else:
        print('you are wrong')
#print('correct percent =',int(correct)/len(quizs)*100,'%')
correct_percent = int(correct)/len(quizs)*100
# data =[
#     ['john',correct percent],

# ]

# pyexcel.save_as(array =data, dest_file_name='quiz.xlsx')
#print(quiz['choices'][1])