#!/usr/env python
#coding=utf8

# NOTE This is not to be used as it's not complete.
from sys import exit
exit()
# TODO Finish, maybe?

from sys import argv
from distutils.core import setup

def main():
    if argv[1] == 'install':
        setup(name         = 'AllPass',                      
              version      = '1.0',
              description  = 'Password manager',
              author       = 'Haukur Páll Hallvarðsson',
              author_email = 'haukurpallh@gmail.com',
              py_modules   = ['allpass'])

if __name__ == '__main__':
    main()
