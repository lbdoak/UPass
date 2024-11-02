import pyperclip
from manager import connect, store_pass, del_pass, find_user, find_pass
from encryption import gen_password
import os

def menu():
    print(('-'*13) + 'MENU' + ('-' *13))
    print('1. Manually create a new entry')
    print('2. Generate a secure password')
    print('3. Delete an entry')
    print('4. Find a password for a site or app')
    print('5. Find all sites and apps connected to a user or email')
    print('q. Exit')
    print('-'*30)
    return input(': ')

def create():
    data = {}
    print(('-'*12) + 'CREATE' + ('-' *12))
    data[0] = input('Enter the site or application you wish to save a password for: ')
    data[1] = input('Enter your password: ')
    data[2] = input('[OPTIONAL] Enter an email, or press ENTER to continue: ')
    data[3] = input('[OPTIONAL] Enter a username, or press ENTER to continue: ')
    data[4] = input('[OPTIONAL] Enter a site url, or press ENTER to continue: ')
    clear()
    store_pass(data[3], data[2], data[1], data[4], data[0], connect())

def generate():
    print(('-'*11) + 'GENERATE' + ('-' *11))
    len = input('Enter the desired length of the secure password: ')
    print('-'*30)
    password = gen_password(len)
    pyperclip.copy(password)
    clear()
    print('Your password has been copied to your clipboard! Your password is:\n')
    print('-'*30)
    print('')
    print(password)
    print('')
    print('-'*30)
    print('')

def remove_entry():
    print(('-'*12) + 'DELETE' + ('-' *12))
    app = input('Enter the app/site for this entry: ')
    user = input('Enter the user/email for this app/site: ')
    clear()
    del_pass(user, app, connect())

def search_pass():
    print(('-'*10) + 'PSWDSEARCH' + ('-' *10))
    password = input('Enter password to search for: ')
    clear()
    print(('-'*10) + 'PSWDSEARCH' + ('-' *10))
    print('Finding matches...\n')
    find_pass(password, connect())

def search_user():
    print(('-'*10) + 'USERSEARCH' + ('-' *10))
    user = input('Enter username or email to search for: ')
    clear()
    print(('-'*10) + 'USERSEARCH' + ('-' *10))
    print('Finding matches...\n')
    find_user(user, connect())

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')