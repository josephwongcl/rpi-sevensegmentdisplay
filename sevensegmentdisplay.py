#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

####################
# Inits
####################

# GPIO Inits
GPIO.setmode(GPIO.BOARD)

# Constants
GPIO_PIN_NUMBER = [3,5,7,8,10,11,12]

for x in GPIO_PIN_NUMBER:
    GPIO.setup(x, GPIO.OUT)

#GPIO.setup(3, GPIO.OUT) #f
#GPIO.setup(5, GPIO.OUT) #g
#GPIO.setup(7, GPIO.OUT) #e
#GPIO.setup(8, GPIO.OUT) #c
#GPIO.setup(10, GPIO.OUT) #b
#GPIO.setup(11, GPIO.OUT) #d
#GPIO.setup(12, GPIO.OUT) #a

userInput = ""

####################
# Functions
####################

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def gpio_clear():
    for i in GPIO_PIN_NUMBER:
        GPIO.output(i, False)

def gpio_turn_on(num):
    GPIO.output(num, True);

def gpio_read_letters(letters):
    for x in letters:
        if x == 'a':
            gpio_turn_on(12);
        elif x == 'b':
            gpio_turn_on(10);
        elif x == 'c':
            gpio_turn_on(8);
        elif x == 'd':
            gpio_turn_on(11);
        elif x == 'e':
            gpio_turn_on(7);
        elif x == 'f':
            gpio_turn_on(3);
        elif x == 'g':
            gpio_turn_on(5);

def gpio_show_number(num):
    if num == 0:
        gpio_read_letters("abcdef")
    if num == 1:
        gpio_read_letters("bc")
    if num == 2:
        gpio_read_letters("abged")
    if num == 3:
        gpio_read_letters("abgcd")
    if num == 4:
        gpio_read_letters("fgbc")
    if num == 5:
        gpio_read_letters("afgcd")
    if num == 6:
        gpio_read_letters("afgecd")
    if num == 7:
        gpio_read_letters("abc")
    if num == 8:
        gpio_read_letters("abcdefg")
    if num == 9:
        gpio_read_letters("abcfg")

def user_quit():
    gpio_clear()
    GPIO.cleanup()
    print "Buh-bye"

def user_clear():
    gpio_clear()

def user_help():
    print "h         - Help | What you are currently seeing"
    print "q         - Quit | Quit the application"
    print "<number>  - Displays <number> | Changes what number the LED shows to <number>"
    print "c         - Clear | Clears all LEDs"

def main():
    print "Enter a command (type \'h\' for help):"
    while 1:
        userInput = raw_input("> ");
        gpio_clear()
        if (userInput == "q"):
            user_quit()
            break
        elif (userInput == "c"):
            user_clear()
        elif (userInput == "h"):
            user_help()
        elif (len(userInput) == 1 and is_number(userInput)):
            number = int(userInput)
            print "DEBUG: SAFE"
            gpio_show_number(number)
        elif (userInput == "cd"):
            print "COUNTDOWN!"
            for x in range(0,10):
                x = 9 - x
                gpio_show_number(x)
                sleep(0.5)
                gpio_clear();
        else:
            print "Invalid command, type \'h\' for help"

#
# Main - start here
#

test = "0"

print len(test) == 1
print is_number(test)
print test
print int(test)
print int(test) + 9
main()
