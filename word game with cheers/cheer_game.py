
# This program/mini game asks  the user to pick a word randomly out of the four listed words, 
# if the word is generated, it plays a cherrs up sound.

# Music from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;
# utm_campaign=music&amp;utm_content=6713">Pixabay</a>

#Dependency

#playsoud library.
#random module

########################################################################################################

from playsound import playsound
import random

username = input('Enter you username:  ')
counter = int(input('How times do you want to play?   '))
overall = counter * 5
total = 0  #initailizing the score, 5 points per each correct guess.

def guess_word():
    word_list = ['John']#, 'Osita', 'Amit', 'Jerry']  #list of words
    print(f'Choose a word from these words: {word_list}')
    word = input('Enter the word: ').capitalize()
    if word in word_list: 
        word_we_got = random.choice(word_list) #generating word
        if word_we_got == word:   #comparing words
            print('Correct')
            playsound("C://Users//user//Desktop//PUSH2GITHUB//word game with cheers//crowd_cheers.mp3")
            global total
            total += 5
        else:
            print(f' We got {word_we_got} Please, Try again')

    else:
        print('Word not on the list') 

while 0 < counter:
    guess_word()
    counter -=1
print(f" Thank you for you time {username}; hope you had fun?\n you scored {total}/{overall}. ")   

###################################################################################################################

