#simple login system
"""
Notes: Saving and loading database of class Login manually through my own method.
    Module pickle or json would be a better choice to store and load
"""

import os
import pickle

database = []

class Login():
    def __init__(self, first, last, username, email, password):
        self.first = first
        self.last = last
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.first} ' + self.last + '\n' + f'{self.username} - {self.email} - {self.password}'

    def dump(self):
        return f'{self.first},{self.last},{self.username},{self.email},{self.password}\n'

def loginLoad(database):
    if os.path.exists('userInfo.txt'):
        
        try:
            with open('userInfo.txt', 'r') as f:
                for line in f:
                    word = ''
                    data = []
                    for x in line:
                        if x == ',' or x == '\n':
                            data.append(word)
                            word = ''
                        else:
                            word += x
                    database.append(Login(data[0], data[1], data[2], data[3], data[4]))
        except (FileNotFoundError, IndexError):
            pass

def loginScreen():
    notFound = True
    while notFound:
        username = input('Username: ')
        password = input('Password: ')

        if (username not in [login.username for login in database]):
            print('No user found by that name. Try again.')
        else:
            for x in database:
                if x.username == username:
                    if x.password == password:
                        print('Login successful')
                        notFound = False
                    else:
                        print("Passwords don't match. Try again.")

def addLogin():
    first = input('First name: ')
    last = input('Last name: ')
    username = input('Username: ')
    email = input('Email: ')
        
    while True:
        password = input('Password: ')
        passCheck = input('Please reenter password: ')
        if password != passCheck:
            print('Try Again, Passwords do not match')
            continue
        else:
            break

    if (email not in [login.email for login in database]):
        database.append(Login(first, last, username, email, password))
        with open('userInfo.txt', 'w') as f:
            for login in database:
                f.write(login.dump())
    else:
        print('Sorry that email is already taken.')
        addLogin()

def splashScreen():
    print('*******Login System*******')

    while True:
        try:
            ans = int(input('login(1) or new account(2): '))
        except ValueError:
            print('Please enter 1 or 2')
        else:
            break

    if ans == 1:
        loginScreen()
    elif ans == 2:
        addLogin()

    splashScreen()

loginLoad(database)

splashScreen()