AllPass
=========

Features
--------
Generate secure, portable and unique passwords for every website. All you need
to remember is a singe "master" password. The program will generate different
passwords depending on your input, that is, the seeds you enter on runtime.

Setup
-----
### Installing on Linux
Open a terminal and execute the following commands:

    $ cd ~/Downloads/AllPass # cd to the folder containing the source files.
    $ mkdir ~/.allpass
    $ cp *.* ~/.allpass

Modify `$USER` in the following lines to your username:

    $ echo alias k="python /home/$USER/.allpass/allpass.py >> ~/.bashrc"
    $ echo alias ko="python /home/$USER/.allpass/allpass.py -o >> ~/.bashrc"

Close the terminal and open it anew. Type `k` to run the program normally, `ko`
to run it with the parameter -o (additional options).

Usage
-----
To run the program simply type `k` in the terminal. Additional options are
available by typing `ko` or by running the program with the parameter `-o`. On
runtime you're asked for two seeds (or more via `-o` if you wish). The first
seed may be called your "master password", which you should use for all the
passwords you wish to generate. The second seed may be called the "ID" of the
password you want to generate. This means that all you have to remember to
generate the same password is the master password (preferably the same for all
your passwords) and the password's ID. Example:

    $ k
    AllPass - Your passwords everywhere and nowhere.
    Seed #1:
    Seed #2:
    Password saved to the clipboard. Press enter to clear it and exit.

Or alternatively:

    $ ko
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

As you may have noticed the text on the "Seed #x" lines is hidden. The program
does this automatically in case someone is sitting beside you.


