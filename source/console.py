from interface import menu, create, generate, remove_entry, search_pass, search_user, clear
from encryption import gen_master
import pyperclip
import time

res, secret = gen_master()
if res == True:
    for i in range(0, 3):
        master = input('Please enter the master password to use PassMan.\n\n')
        if master in secret:
            print('Welcome to PassMan!\n')
            break
        elif i == 2:
            clear()
            print('Security Protocol Triggered, Access Denied.')
            time.sleep(1.5)
            exit()
            exit()
        else:
            print(f'\nIncorrect Master Key. {2 - i} chances remaining.\n')
else:
    pyperclip.copy(secret)
    print('Welcome to PassMan! Your personal Master Key to access PassMan is:')
    print('-'*30)
    print('')
    print(secret)
    print('')
    print('-'*30)
    print('')
    print('Please record this master key, as it cannot be recovered for security purposes. It has been added to your clipboard for convenience.')
    input('\nPress any key to proceed.\n')
    clear()

while True:
    input = menu()
    clear()
    if input == '1':
        create()
        continue
    if input == '2':
        generate()
        continue
    if input == '3':
        remove_entry()
        continue
    if input == '4':
        search_pass()
        continue
    if input == '5':
        search_user()
        continue
    if input == 'q':
        exit()
    else:
        print(f'\nInvalid Option "{input}". Please refer to menu.\n')