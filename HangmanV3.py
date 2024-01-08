"""
Hangman Game

Objective:
Guess the letters in the word, and beat the high score

Controls:
Press any letter to guess a letter, press 1 to use a hint

Author: Martins Iwuogor

Date: December 28, 2023

"""

import random




Hangman = [
'''     _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___ ''',
'''       _______
     |/      |
     |      (_)
     |      \|
     |       
     |
     |
 jgs_|___ ''',
'''       _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 jgs_|___ ''',
 '''       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 jgs_|___ ''',
 '''       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___ ''',
'''       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / |
     |
 jgs_|___ ''']

print("\n" * 100)
print('''
  _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''')

print("\nWELCOME TO HANGMAN\n")
name = input("What's your name : ")
print(f"Welcome {name}\n")

press = input("Press 1 if you want to guess countries: \nPress 2 if you want to guess words: \n")
countries = ["iran", "afghanistan", "germany", "england", "usa",
             "spain", "croatia", "korea", "japan", "portugal", "malta",
             "ukraine", "china", "ireland", "iceland", "nigeria",
             "ghana", "sudan", "guinea", "france", "italy", "senegal",
             "slovakia", "slovenia", "egypt", "cameroon", "iraq", "sweden", "denmark",
             "argentina", "romania", "brazil", "uzbekistan", "poland", "madagascar",
             "thailand", "canada", "israel", "pakistan", "palestine", "india", "australia", "new zealand"]

word = ["letter", "food", "jesus", "strength", "car", "apple",
        "orange", "fish", "lion", "goat", "application", "venison",
        "stomach", "great", "joy", "love", "peace", "harvest",
        "tree", "skeleton", "cheat", "mathematics", "cross", "street"]

randCountries = random.choice(countries)
listCountries = list(randCountries)
blankSpace = "_"
lenCountry = len(randCountries)
blankCountry = blankSpace * lenCountry
listBlankCountry = list(blankCountry)

r_word = random.choice(word)
l_word = list(r_word)
space = "_"
lenWord = len(r_word)
spacedWord = space * lenWord
listSpacedWord = list(spacedWord)


i = 0  # index of the hangman aschi art
h = "_______"  # string that has 7 dashes
G = list(h)    # the list for the above string
Z = list(Hangman)   # the list for the hangman aschi art, which has a length of 7 as well
j = 1  # Game levels
highScore = 0  # Game High Scores
best = 220  # Current Highest Score or Best Score
hints = 0   # number of hints
firstDisplay = 0  # first display of the aschi art


# the game ends when the hangman aschi art image is complete, so for every wrong guess, an element in the
# hangman list which is "Z" is substituted with the corresponding index element in the "G" list, so the
# loop continues until the last element in the Z list is substitutes the last elements in the G list, therefore
# ending the loop


# loop to guess countries
while press == "1" and G[5] != Z[5]:

    if firstDisplay == 0:
        print("\nDASH BOARD:\nGuess the letters in this country:\n")
        print(blankCountry)
        print(
'''              _______
             |/      |
             |      (_)
             |      
             |       
             |      
             |
         jgs_|___ ''')
    firstDisplay += 1


# Resets the hangman when moving to a new level
    if "_" not in listBlankCountry:
        randCountries = random.choice(countries)
        listCountries = list(randCountries)
        blankSpace = "_"
        lenCountry = len(randCountries)
        blankCountry = blankSpace * lenCountry
        listBlankCountry = list(blankCountry)
        i = 0
        h = "_______"
        G = list(h)
        Z = list(Hangman)
        p = ""

# Displays available hints on the dashboard
    if hints == 0:
        print("\nHints : \n(_) (_) (_) (_)\n")
    elif hints == 1:
        print("\nHints : \n(_) (_) (_)\n")
    elif hints == 2:
        print("\nHints : \n(_) (_)\n")
    elif hints == 3:
        print("\nHint : \n(_)\n")

# Displays a prompt to type any letter or use an hint
    letter = input("\nGuess a letter (or press 1 for a hint) : ")

# Displays a prompt that tells when your hints are finished
    if letter == "1" and hints == 4:
        print("You have exhausted your hints, you can no longer use any")
        letter = "2"

# How the hint feature works
    elif letter == "1" and letter not in listCountries:
        p = random.choice(listCountries)
        if p not in ''.join(listBlankCountry):
            index = listCountries.index(p)
            listBlankCountry[index] = p
            print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this country:\n\n", ''.join(listBlankCountry))
            print(Hangman[i])
            hints += 1

        elif p in ''.join(listBlankCountry):
            while p in ''.join(listBlankCountry):
                p = random.choice(listCountries)
            index = listCountries.index(p)
            listBlankCountry[index] = p
            print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this country:\n\n", ''.join(listBlankCountry))
            print(Hangman[i])
            hints += 1


# When a letter is guessed incorrectly
    elif letter not in randCountries:
        print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this country:\n\n", ''.join(listBlankCountry))
        G[i] = Z[i]
        print(f"You guessed {letter}, that's not in the word. You lose a life")
        print(Hangman[i])
        if G[5] == Hangman[5]:
            print(f"\nSorry {name} is GAME OVER!, YOU LOSE!, The word was actually {randCountries.upper()}")
            if highScore > best:
                print(f"Your final score is {highScore}\nCongrats You Have The New High Score!")
                break
            else:
                print(f"Your final score is {highScore}\nThe high score is {best} still held by Martins")
                break
        i += 1

# When a letter is guessed correctly
    elif letter in randCountries:
        for n in range(0, len(randCountries)):
            if letter == randCountries[n]:
                listBlankCountry[n] = randCountries[n]
                print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this country:\n\n", ''.join(listBlankCountry))
                print(Hangman[i])
                lenCountry -= 1
                if "_" not in listBlankCountry:
                    j += 1
                    print(f"\nCorrect!, YOU MOVE TO LEVEL {j}")
                    highScore += 20
                    print(f"Your current High Score is {highScore}, keep going!...press any letter to continue")


# loop to guess words, it contains same features with the country version
while press == "2" and G[5] != Z[5] :

    if firstDisplay == 0:
        print("\nDASH BOARD:\nGuess the letters in this word:\n")
        print(spacedWord)
        print(
'''                _______
             |/      |
             |      (_)
             |      
             |       
             |      
             |
         jgs_|___ ''')

    firstDisplay += 1

    if "_" not in listSpacedWord:
        r_word = random.choice(word)
        l_word = list(r_word)
        space = "_"
        lenWord = len(r_word)
        spacedWord = space * lenWord
        listSpacedWord = list(spacedWord)
        i = 0
        h = "_______"
        G = list(h)
        Z = list(Hangman)
        p = ""

    if hints == 0:
        print("\nHints : \n(_) (_) (_) (_)\n")
    elif hints == 1:
        print("\nHints : \n(_) (_) (_)\n")
    elif hints == 2:
        print("\nHints : \n(_) (_)\n")
    elif hints == 3:
        print("\nHint : \n(_)\n")

    letter = input("\nGuess a letter (or press 1 for a hint) : ")
    if letter == "1" and hints == 4:
        print("You have exhausted your hints, you can no longer use any")
        letter = "2"

    elif letter == "1" and letter not in l_word:
        p = random.choice(l_word)
        if p not in ''.join(listSpacedWord):
            index = l_word.index(p)
            listSpacedWord[index] = p
            print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this word:\n\n", ''.join(listSpacedWord))
            print(Hangman[i])
            hints += 1

        elif p in ''.join(listSpacedWord):
            while p in ''.join(listSpacedWord):
                p = random.choice(l_word)
            index = l_word.index(p)
            listSpacedWord[index] = p
            print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this word:\n\n", ''.join(listSpacedWord))
            print(Hangman[i])
            hints += 1

    elif letter not in r_word:
        print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this word:\n\n", ''.join(listSpacedWord))
        G[i] = Z[i]
        print(f"You guessed {letter}, that's not in the word. You lose a life")
        print(Hangman[i])
        if G[5] == Hangman[5]:
            print(f"\nSorry {name} is GAME OVER!, YOU LOSE!, The word was actually {r_word.upper()}")
            if highScore > best:
                print(f"Your final score is {highScore}\nCongrats You Have The New High Score!")
                break
            else:
                print(f"Your final score is {highScore}\nThe high score is {best} still held by Martins")
                break
        i += 1

    elif letter in r_word:
        for n in range(0, len(r_word)):
            if letter == r_word[n]:
                listSpacedWord[n] = r_word[n]
                print("\n" * 100, "\nDASH BOARD:\nGuess the letters in this word:\n\n", ''.join(listSpacedWord))
                print(Hangman[i])
                lenWord -= 1
                if "_" not in listSpacedWord:
                    j += 1
                    print(f"\nCorrect!, YOU MOVE TO LEVEL {j}")
                    highScore += 20
                    print(f"Your current High Score is {highScore}, keep going!...press any letter to continue")


