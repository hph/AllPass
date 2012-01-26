AllPass
=======

Features
--------
Generate secure, portable and unique passwords for every website. All you need
to remember is a singe "master" password. The program will generate different
passwords depending on your input, that is, the seeds you enter on runtime. The
default password length is 16 characters with 7 lowercase characters, 3
uppercase characters, 3 numbers and 3 symbols.

Setup
-----
### Installing on Linux
Open a terminal and execute the following commands:

    $ git clone git://github.com/haukurpallh/AllPass.git
    $ mv AllPass ~/.allpass
    $ echo alias ap="python /home/$USER/.allpass/allpass.py" >> ~/.bashrc
    $ echo alias apo="python /home/$USER/.allpass/allpass.py -o" >> ~/.bashrc

Usage
-----
To run the program simply type `ap` in the terminal. Additional options are
available by typing `apo` or by running the program with the parameter `-o`. On
runtime you're asked for two seeds (or more via `-o` if you wish). The first
seed may be called your "master password", which you should use for all the
passwords you wish to generate. The second seed may be called the "ID" of the
password you want to generate. This means that all you have to remember to
generate the same password is the master password (ideally the same for all
your passwords) and the password's ID. For example:

    $ ap
    AllPass - Your passwords everywhere and nowhere.
    Seed #1: $master
    Seed #2: $id
    Password saved to the clipboard. Press enter to clear it and exit.

Your input isn't visible for safety purposes. If you want, you can
alternatively use the `apo` command:

    $ apo
    AllPass - Your passwords everywhere and nowhere.
    Number of seeds: 3
    Seed #1: 
    Seed #2: 
    Seed #3: 
    Number of lowercase characters: 10
    Number of uppercase characters: 5
    Number of digits: 4
    Number of symbols: 4
    Password saved to the clipboard. Press enter to clear it and exit.
