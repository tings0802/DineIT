#!/usr/bin/python3

import os, time, random
from datetime import datetime

def read(path='data.txt'):
    raw = data = []
    with open(path, 'r') as file:
        raw = file.readlines()
    
    for item in raw:
        data.append(item.split()[0].split(','))
        for i in range(1, len(data[-1])):
            data[-1][i] = float(data[-1][i])
    return data

def write(data, path='test.txt'):
    content = ''
    if data:
        for item in data:
            for i in range(1, len(item)):
                item[i] = str(item[i])
            content += ','.join(item) + '\n'
    with open(path, 'w') as file:
        file.write(content)

def show(menu, prompt='All stores:'):
    if menu:
        print (prompt)
        for item in menu:
            print(f'{item[0]}')
    else:
        print('The list is empty now.\n')
    print()

def reset(menu):
    # os.system('clear')
    print('Data is reset!\n')
    return menu.clear()

def input_time(prompt, default):
    business_hour = -1
    try:
        business_hour = float(input(prompt))
        while not 0 <= business_hour <= 24:
            print('invalid time input')
            business_hour = float(input(prompt))
    except:
        business_hour = default
    return business_hour

def add(menu):
    store = input('Add one new store ......')
    if store not in menu:
        open_hour = input_time('Add open_hours ...... (ex: 7.25)', 0)
        close_hour = input_time('Add close_hours ...... (ex: 16.30)', 24)
        menu.append([store, open_hour, close_hour])
    # os.system('clear')
    print ('Data is update!\n')
    return menu

def delete(menu):
    store = input('Delete one store ......')
    menu = [item for item in menu if store != item[0]]
    # os.system('clear')
    print ('Data is update!\n')
    return menu

def filter(menu):
    now = datetime.now().hour +  datetime.now().minute * 0.01
    new_menu = []
    for item in menu:
        for i in range(1, len(item), 2):
            if item[i] < now < item[i + 1]:
                new_menu.append(item)
                break
    return new_menu

def choose(menu):
    if menu:
        return random.choice(menu)[0]
    # os.system('clear')
    print('The list is empty now.\n')

def main():
    option = '\n'.join(['(E)xecute program',
                        '(L)ist all stores',
                        '(A)dd store',
                        '(D)elete store',
                        '(R)eset data',
                        '(Q)uit'])
    path = 'data.txt'
    menu = read(path)
    os.system('clear')
    command = ''
    while command.lower() not in ['quit', 'q']:
        show(filter(menu), 'now available:')
        print(option)
        command = input('Let\'s choose what to eat ......').lower()
        os.system('clear')
        if command in ['show', 's', 'list', 'ls', 'l']:
            show(menu)
        elif command in ['append', 'add', 'a']:
            menu = add(menu)
        elif command in ['delete', 'del', 'd']:
            menu = delete(menu)
        elif command in ['execute', 'exe', 'e']:
            print(choose(filter(menu)))
        elif command in ['reset', 'r']:
            menu = reset(menu)
        elif command in ['quit', 'q']:
            print ('Thanks for your visit!')
        else:
            print('invalid option input')
    write(menu)

def test(path='data.txt'):
    menu = read()
    show(menu)
    write(menu)

if __name__ == '__main__':
    main()
    # test()