
word = input('play word')
list_word = list(word)
# print(list_word)
import random
random.shuffle(list_word)
for i in range(len(list_word)):
    print(list_word[i],end=' ')
chuan = True
While chuan:
    answer = input('your answer?')
    if answer == word:
        chuan = False
        print('you are correct')
    else:
        print('your are wrong' )

