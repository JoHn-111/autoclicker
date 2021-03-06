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

def clicker():
    i = 0
    global cclick, mytime, stop
    while i < cclick:
        time.sleep(mytime)
        m.click(button='left')
        i += 1
        if i == cclick:
            quit()
        elif k.is_pressed(stop):
            quit()

def clicker_speed_2():
    i = 0
    global cclick, mytime, stop
    while i < cclick:
        time.sleep(mytime)
        m.double_click(button='left')
        i += 1
        if i == cclick:
            quit()
        elif k.is_pressed(stop):
            quit()

def whillle():
    while True:
        if k.is_pressed(start):
            clicker()

def speed_2():
    while True:
        if k.is_pressed(start):
            clicker_speed_2()
#russian lang
def mode_lang_ru():
    try:
        global cclick, mytime
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
    global stop, start, speed 
    start = input('Выберите кнопку включения: ')
    stop = input('Выберите кнопку выключения: ')
    speed = input('Выберите режим скорости и количества кликов 2х("2") или нажмите "Enter": ')
    if speed == '2':
        speed_2()
    elif speed == '':
        whillle()
#english lang
def mode_lang_en(): 
    global cclick, mytime      
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
    global stop, start, speed
    start = input('Choose a power button on: ')
    stop = input('Choose a power button off: ')
    speed = input('Select the speed mode and the number of clicks 2x ("2") or press "Enter"')
    if speed == '2':
        speed_2()
    elif speed == '':
        whillle()

def lang():
    compatibility = input("Choose your mode. Try compatibility mode (English language without ASCII)\nEnter \"c\" for compatibility mode. Enter \"x\" for normal mode: ")
    if compatibility == "c":
        clear()
        mode_lang_en()
    elif compatibility == "x":
        clear()
        mode_lang_ru()
    if compatibility == "с":
        clear()
        mode_lang_en()

lang()

