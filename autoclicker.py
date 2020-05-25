import os
import mouse as m
import keyboard as k
import time


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear()


def mode_lang_ru():
    try:
        click = input('Введите количество кликов: ')
        c = click.replace(',', '.').split()
        cclick = float(c[0])
        my_time = input('Введите задержку между кликами(в секундах): ')
        t = my_time.replace(',', '.').split()
        mytime = float(t[0])
    except ValueError:
        print('Вы ввели не число!')
        time.sleep(3)
        quit()

    start = input('Выберите кнопку включения: ')
    stop = input('Выберите кнопку выключения: ')

    

    def clicker():
        i = 0
        while i < cclick:
            time.sleep(mytime)
            m.double_click(button='left')
            i += 1
            if i == cclick:
                quit()
            elif k.is_pressed(stop):
                quit()
    while True:
        if k.is_pressed(start):
            clicker()

def mode_lang_en():
    try:
        click = input('Enter the desired number of clicks: ')
        c = click.replace(',', '.').split()
        cclick = float(c[0])
        my_time = input('Set the delay between clicks(in seconds): ')
        t = my_time.replace(',', '.').split()
        mytime = float(t[0])
    except ValueError:
        print('You entered not a number!')
        time.sleep(3)
        quit()

    start = input('Choose a power button on: ')
    stop = input('Choose a power button off: ')

    

    def clicker():
        i = 0
        while i < cclick:
            time.sleep(mytime)
            m.double_click(button='left')
            i += 1
            if i == cclick:
                quit()
            elif k.is_pressed(stop):
                quit()
    while True:
        if k.is_pressed(start):
            clicker()


def lang():
    compatibility = input(
        "Choose your mode. Try compatibility mode (English language without ASCII\nEnter c for compatibility mode. Enter x for normal mode: ")
    if compatibility == "c":
        clear()
        mode_lang_en()
    elif compatibility == "x":
        clear()
        mode_lang_ru()

lang()
