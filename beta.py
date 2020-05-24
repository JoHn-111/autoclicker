import os
import mouse as m
import keyboard as k
import time



def clear ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



one = "one", two = "two", three = "three", four = " ", five = " ", another = "another"

def mode():
    println("Type c for compatibility mode. Any another key for normal mode")
    compatibility = input(Choose your mode. Try compatibility mode (English language without ASCII) if the program crashes in normal mode. Type c for compatibility mode. Any another key for normal mode")
if compatibility = c
    one = "Enter the desired number of clicks"
    two = "Set the delay"
    three = "you're retard, lmao"
    another = "it's work)"
else
    one = "Задайте количество кликов"
    two = "Установите задержку между кликами"
    three = "Вы ввели не число, попробуйте ещё раз"
    four = "Задайте кнопку включения"
    five = "Задайте кнопку выключения"
    another = 

def main ()

clear ()
main()


try:
	click = input(one)
	c = click.replace(',', '.').split()
	cclick = float(c[0])
	my_time = input(two)
	t = my_time.replace(',', '.').split()
	mytime = float(t[0])
except ValueError:
	print(three)
	time.sleep(3)
	quit()

start = input(four)
stop = input(five)


i = 0
def clicker():
	global i
	while i < cclick:
		time.sleep(mytime)
		m.click(button ='left')
		i += 1
		
		if i == cclick:
			quit()	
		elif k.is_pressed(stop):
			quit()

while True:
	if k.is_pressed(start):
		clicker()
