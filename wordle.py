import os
import random

subject = input("Choose The Topic: mixed||sport||food \n")
script_directory = os.path.dirname(os.path.abspath(__file__))
bank = os.path.join(script_directory, subject)

def load_words(path):
    with open(path,'r') as file:
        words = file.read().split('\n')
    return words


def choose_word():
    words = load_words(bank)
    line = random.randint(0,49)
    word = words[line]
    return word


def guess():
    answer = choose_word()
    word = "*****"
    print("\nThe Game Begins!\nEnter 'exit' To Leave The Game\n")
    while ('*' in word):
        guess = input("enter a word: ")
        for i in range(5):
            if guess == 'exit':
                print("The Answer Is", answer)
                return -1
            elif len(guess) == 5:
                if guess[i] == answer[i]:
                    word = word[:i] + answer[i] + word[i + 1:]
                elif guess[i] in answer:
                    if guess[i] not in word:
                        print(guess[i] , 'is in the word')
            else:
                print("The Word Is 5 Letters Long\nTry Again")
                guess = input("enter a word: ")
        print(word)
    print("Good Job!! The Word Is", word)        

guess()