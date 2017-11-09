#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:15:24 2017

course: MITx 6.00.1x: Introduction to Computer Science and Programming Using Python
source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017
"""

"""
Problem Set 3 - Problem 4 - Printing Out all Available Letters

Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
 This starts up an interactive game of Hangman between the user and the computer. 
 Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
    
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) 
 to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. 
 When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

    guess = 'A'
    guessInLowerCase = guess.lower()
    
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

    1. secretWord: The word to guess.
    
    2. lettersGuessed: The letters that have been guessed so far.
    
    3. mistakesMade: The number of incorrect guesses made so far.
    
    4. availableLetters: The letters that may still be guessed. 
        Every time a player guesses a letter, the guessed letter must be removed from availableLetters 
         (and if they guess a letter that is not in availableLetters, you should print a message telling 
         them they've already guessed that - so try again!).
         
"""


"""Solution"""
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    test = True
    for l in secretWord:
        if l in lettersGuessed:
            test = test and True
        else:
            return False
    return test

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    final = ''
    for l in secretWord:
        if l in lettersGuessed:
            final += l
        else:
            final += '_ '
    return final

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = 'abcdefghijklmnopqrstuvwxyz'
    final = ''
    for l in available:
        if l not in lettersGuessed:
            final = final + l
    return final

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 0
    lettersGuessed = []
    availableLetters = getAvailableLetters([])
    letter = ''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    
    while mistakesMade < 8 and not isWordGuessed(secretWord,lettersGuessed):
        print("------------")
        print("You have " + str(8-mistakesMade) + " guesses left")
        print("Available Letters: " + availableLetters)
        letterOrig = input("Please guess a letter: ")
        letter = letterOrig.lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif letter in secretWord:
            lettersGuessed.append(letter)
            availableLetters = getAvailableLetters(lettersGuessed)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(letter)
            availableLetters = getAvailableLetters(lettersGuessed)
            mistakesMade += 1

    if mistakesMade == 8:
        print("------------")
        print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")
    else:
        print("------------")
        print("Congratulations, you won!")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)