#!/usr/bin/env python
#coding=utf8

# TODO
# pwd_strength()
# import optparser
# import setupdrasl
# setup shit..
# ...

import random
import string
from getpass import getpass
from gtk import clipboard_get
from sys import argv

def password(seed, lowercase=4, uppercase=4, digits=4, symbols=4):
    ''''''
    rand_str = lambda len: ''.join(sample(letters + digits + punctuation, len))
    in_chars = lambda chars: any([1 for x in xrange(1,10) if str(x) in chars])
    random.seed(seed)
    password = rand_str(16)
    return password if in_chars( # breyta in_chars, check for any for all.

def generate_password(seed, lowercase=7, uppercase=3, digits=3, symbols=3):
    '''Generates and returns a password based upon an input seed.'''
    # NOTE A simpler and yet acceptable way to do this would be
    # ''.join(sample(lowercase + uppercase + digits + punctuation, 16))
    random.seed(seed)
    password = ''
    for _ in xrange(lowercase):
        password += random.choice(string.lowercase)
    for _ in xrange(uppercase):
        password += random.choice(string.uppercase)
    for _ in xrange(digits):
        password += random.choice(string.digits)
    for _ in xrange(symbols):
        password += random.choice(string.punctuation)
    return ''.join(random.sample(password, len(password)))

def set_clipboard(text):
    '''Sets text as the clipboard.'''
    clipboard = clipboard_get()
    clipboard.set_text(text)
    clipboard.store()

def main():
    # NOTE Add more options and improve error handling.
    # TODO Add more features.
    try:
        print 'AllPass - Your passwords everywhere and nowhere.'
        if '-o' in argv:
            number_of_seeds = int(raw_input('Number of seeds: '))
            if number_of_seeds >= 1:
                list_of_seeds = []
                for number in xrange(number_of_seeds):
                    list_of_seeds.append(getpass('Seed #%i: ' % (number + 1)))
                seed = tuple(seed for seed in list_of_seeds)
            else:
                seed = ''
            lowercase = int(raw_input('Number of lowercase characters: '))
            uppercase = int(raw_input('Number of uppercase characters: '))
            digits = int(raw_input('Number of digits: '))
            symbols = int(raw_input('Number of symbols: '))
            generate_password(seed, lowercase, uppercase, digits, symbols)
        else:
            generate_password((getpass('Seed #1: '), getpass('Seed #2: ')))
        print 'Password saved to the clipboard.',
        raw_input('Press enter to clear it and exit.')
        set_clipboard('')
    except:
        print 'Error!'

if __name__ == '__main__':
    main()
