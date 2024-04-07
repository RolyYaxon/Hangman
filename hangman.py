import random
from words import words
import string

def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        
        print ("lives", lives, "you used this letters", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives -1
                print("Letter no in the word")

        elif user_letter in used_letters:
            print ("you have used this letter")
            
        else: 
            print("Please enter a valid letter")
            
    if lives == 0:
        print("No lives, the word was: ", word) 
    else:
        print("you did it ", word )
hangman()