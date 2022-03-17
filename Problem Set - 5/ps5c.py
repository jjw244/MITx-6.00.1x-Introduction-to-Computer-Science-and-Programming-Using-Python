#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:15:24 2017

course: MITx 6.00.1x: Introduction to Computer Science and Programming Using Python
source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017
"""

"""
Problem Set 5 - Problem 3 - CiphertextMessage
Instructions:
    
For this problem, the graders will use our implementation of the Message and PlaintextMessage classes, 
 so don't worry if you did not get the previous parts correct.

Given an encrypted message, if you know the shift used to encode the message, 
 decoding it is trivial. If message is the encrypted message, and s is the shift 
 used to encrypt the message, then apply_shift(message, 26-s) gives you the original plaintext message. 
 Do you see why?

The problem, of course, is that you don’t know the shift. But our encryption method 
 only has 26 distinct possible values for the shift! 
 We know English is the main language of these emails, so if we can write a program 
  that tries each shift and maximizes the number of English words in the decoded message, we can decrypt their cipher! 
 A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words. 
 Note that this only means that most of the words obtained are actual words. 
 It is possible to have a message that can be decoded by two separate shifts into different sets of words. 
 While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

Fill in the methods in the class CiphertextMessage according to the specifications in ps6.py. 
The methods you should fill in are:

    - __init__(self, text): Use the parent class constructor to make your code more concise.
    
    - decrypt_message(self): You may find the helper function is_word(wordlist, word) 
       and the string method split() useful. Note that is_word will ignore punctuation and 
       other special characters when considering whether a word is valid.
       
Hints:
    
Using string.split

You may find the function string.split useful for dividing the text up into words.
    >>> 'Hello world!'.split('o')
    ['Hell', ' w', 'rld!']
    >>> '6.00.1x is pretty fun'.split(' ')
    ['6.00.1x', 'is', 'pretty', 'fun']
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

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        
        Message.__init__(self, text)
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        
        self.encrypting_dict = self.build_shift_dict(self.shift)
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        
        self.message_text_encrypted = self.apply_shift(self.shift)
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        
        self.last_shift = self.shift
        self.shift = shift
        diff = self.shift - self.last_shift
        
        self.encrypting_dict = self.build_shift_dict(diff)
        self.message_text_encrypted = self.apply_shift(diff)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        best_shift = None
        best_real_words = 0
        best_msg = ""

        for s in range(26):
            decrypted_text = self.apply_shift(s)
            words = decrypted_text.split()
            real_words = sum([is_word(self.get_valid_words(), w) for w in words])
            if real_words > best_real_words:
                best_shift = s
                best_real_words = real_words
                best_msg = decrypted_text

        return (best_shift, best_msg)
            
    
#Example test case (build_shift_dict)
build = Message('hello')
print('Shifted Dictionary:', build.build_shift_dict(2))
    
#Example test case (apply_shift)
shiftedtext = Message('hello')
print('Expected Shifted Text: jgnnq')
print('Actual Shifted Text:', shiftedtext.apply_shift(2))

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())

#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
