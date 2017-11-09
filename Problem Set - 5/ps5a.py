#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:15:24 2017

course: MITx 6.00.1x: Introduction to Computer Science and Programming Using Python
source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017
"""

"""
Problem Set 5 - Problem 1 - Build the Shift Dictionary and Apply Shift
Instructions:
    
The Message class contains methods that could be used to apply a cipher to a 
 string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).

In the next two questions, you will fill in the methods of the Message class found in ps6.py according to the specifications in the docstrings. 
The methods in the Message class already filled in are:

  __init__(self, text)

  The getter method get_message_text(self)

  The getter method get_valid_words(self), notice that this one returns a copy 
   of self.valid_words to prevent someone from mutating the original list.

In this problem, you will fill in two methods:

  1. Fill in the build_shift_dict(self, shift) method of the Message class. 
     Be sure that your dictionary includes both lower and upper case letters, 
      but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. 
     What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".

     If you are unfamiliar with the ordering or characters of the English alphabet, 
      we will be following the letter ordering displayed by string.ascii_lowercase and string.ascii_uppercase:

        >>> import string
        >>> print(string.ascii_lowercase)
        abcdefghijklmnopqrstuvwxyz
        >>> print(string.ascii_uppercase)
        ABCDEFGHIJKLMNOPQRSTUVWXYZ

     A reminder from the introduction page - characters such as the space character, 
       commas, periods, exclamation points, etc will not be encrypted by this 
       cipher - basically, all the characters within string.punctuation, 
       plus the space (' ') and all numerical characters (0 - 9) found in string.digits.

  2. Fill in the apply_shift(self, shift) method of the Message class. 
     You may find it easier to use build_shift_dict(self, shift). 
     Remember that spaces and punctuation should not be changed by the cipher. 
     Also remember that the shifting down the alphabet means to shift "right-ward" towards letters further down in the alphabet..

Paste your implementation of the Message class in the box below.
"""


"""Solution"""
import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        letters = string.ascii_lowercase
        letters_shifted = (letters * 2)[shift : shift + 26]
        letters = letters + letters.upper()
        letters_shifted = letters_shifted + letters_shifted.upper()

        shift_dict = {}

        for i in range(52):
            shift_dict[letters[i]] = letters_shifted[i]
        
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_text = ''
        shift_dict = self.build_shift_dict(shift)

        for char in self.message_text:
            if char in string.ascii_letters:
                char = shift_dict[char]
            shifted_text += char

        return shifted_text
    
#Example test case (build_shift_dict)
build = Message('hello')
print('Shifted Dictionary:', build.build_shift_dict(2))
    
#Example test case (apply_shift)
shiftedtext = Message('hello')
print('Expected Shifted Text: jgnnq')
print('Shifted Text:', shiftedtext.apply_shift(2))
