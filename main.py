import random
import string
from words import words

def getWord(wordsList):
    word = random.choice(words)
    while "-" in word or " " in word:
        word= random.choice(words)
    return word.upper()

def hangman():
    word= getWord(words)
    lettersInWord= set(word)
    alphabet= set(string.ascii_uppercase)
    lettersGuessed= set()
    lives=6
    while len(lettersInWord) > 0 and lives > 0:
        print("\nThe letters you already guessed: ", " ".join(lettersGuessed))
        wordSoFar= [letter if letter in lettersGuessed else "-" for letter in word]
        print("This is what you have so far: ", " ".join(wordSoFar))
        print("You have: " , lives, " chances left")
       

        guess= input("Guess a letter: " ).upper()
        if guess in alphabet - lettersGuessed:
            lettersGuessed.add(guess)
            if guess in lettersInWord:
                lettersInWord.remove(guess)
            else:
                lives-=1
        elif guess in lettersGuessed:
            print("\nPlease type a new letter, this one has been guessed already. ")
        else:
            print("\nWhat you typed is not a letter in the alphabet, please try again")
    
    if lives > 0:
        print("\nCongrats! You won hangman! You guessed the word", word, "correctly!")
    else:
        print("\nSorry, you ran out of chances. The word was", word)

def game():
    playing= True
    valid= False
    while playing:
        hangman()
        while valid is False:
            answer= input("\nWould you like to keep playing? (TYPE Y or N) ").upper()
            valid= check(answer)
        if answer== "N":
            print("\nThank you for playing!")
            playing= False
        

def check(x):
    if x == "Y" or x=="N":
        return True
    else:
        print("Invalid entry. Please type Y or N ")
        return False

if __name__=="__main__":
    game()