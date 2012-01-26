#!/usr/env python
#coding=utf8

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
