from interface import menu, create, generate, remove_entry, search_pass, search_user, display, reset, clear
from encryption import gen_master
from animate import runtime
import pyperclip
import time
from datetime import datetime, timedelta
import subprocess
import os

TIMER = timedelta(minutes=2)

runtime(0)

if os.path.exists('../source/usr/@'):
    with open('../source/usr/@', 'r') as fp:
        lockout = fp.read().strip()
        time_left = datetime.now() - datetime.fromisoformat(lockout)
        if time_left < TIMER:
            print(f"Locked out. Try again in {TIMER - time_left}")
            time.sleep(2)
            runtime(2)
            exit()
        else:
            os.remove('../source/usr/@')

res, secret = gen_master()
if res == True:
    for i in range(0, 3):
        master = input('Please enter the master password to use PassMan.\n\n')
        if master in secret:
            clear()
            print('Welcome to PassMan!\n')
            break
        elif i == 2:
            clear()
            print('Security Protocol Triggered, Access Denied. You will be locked out for 2 minutes. Recurring failures will reset the PassMan to deter attackers')
            time.sleep(1.5)
            runtime(2)
            with open('../source/usr/@', 'w') as fp:
                fp.write(datetime.now().isoformat())
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
    if input == '6':
        display()
        continue
    if input == 'q':
        subprocess.run(["docker-compose", "down"])
        time.sleep(0.5)
        runtime(1)
        exit()
    if input == '!':
        reset()
        print('Resetting and shutting down, please wait...')
        time.sleep(1.5)
        exit()

    else:
        print(f'\nInvalid Option "{input}". Please refer to menu.\n')