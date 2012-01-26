#!/usr/bin/env python
#coding=utf8

from getpass import getpass
from gtk import clipboard_get
from random import choice, sample, seed
from string import lowercase, uppercase, digits, punctuation
from sys import argv

CHR_SET = [lowercase, uppercase, digits, punctuation]

def random_string(len):
    '''Return a random string of lenght 'len'.'''
    return ''.join(choice(''.join(CHR_SET)) for _ in xrange(len))

def strong_password(password):
    '''Return True if 'password' contains at least one lowercase character, one
    uppercase character, one digit and one symbol. Otherwise return False.'''
    in_chrs = lambda chrs: any(True for chr in password if chr in chrs)
    # Check if there's at least one character from each character subset.
    return all(in_chrs(chr_subset) for chr_subset in CHR_SET)

def set_clipboard(text):
    '''Sets text as the clipboard.'''
    clipboard = clipboard_get()
    clipboard.set_text(text)
    clipboard.store()

def allpass(secret_seed, lower=False, upper=False, digits=False, punct=False):
    '''Generate and return a password based on 'seed'.'''
    # NOTE This function doesn't need to be divided into two sections, but the
    # random_string function is needed elsewhere anyway...
    # Also, the code below needs to be rewritten as it's ugly as hell.
    seed(secret_seed)
    if any([lower, upper, digits, punct]):
        password = ''
        for arg in [lower, upper, digits, punct]:
            password += ''.join(choice(chrs) for _ in xrange(arg) for chrs in
                                CHR_SET)
        password = ''.join(sample(password, len(password)))
    else:
        # Why did I do it this way?
        while True:
            password = random_string(16)
            if strong_password(password):
                break
    return password

def main():
    # TODO:
    # - Use optparser and hashlib and restructure accordingly.
    # - Use configparser for settings and salted hash storage?
    # - Improve error handling.
    # - Add features, such as generating a random string with random_string.
    # - Write a setup program.
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
            password = allpass(seed, lowercase, uppercase, digits, symbols)
            set_clipboard(password)
        else:
            password = allpass((getpass('Seed #1: '), getpass('Seed #2: ')))
            set_clipboard(password)
        print 'Password saved to the clipboard.',
        raw_input('Press enter to clear it and exit.')
        set_clipboard('')
    except:
        print 'Error!'
        set_clipboard('')

if __name__ == '__main__':
    main()
