# !/usr/bin/env python

import curses
import time
from quotes import get_quote


VALIDS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

minutes = None
wpm = None


def menu(stdsrc):
    '''
    Main menu
    '''

    options = ['Start Typing', 'Exit']
    selected = 0

    while True:
        # Clear the screen
        stdsrc.clear()

        # Get width and height of the screen
        height, width = stdsrc.getmaxyx()

        # Center the options
        for i, option in enumerate(options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(options) // 2 + i

            # Highlight the selected option
            if i == selected:
                stdsrc.addstr(y, x, option, curses.color_pair(3))

            else:
                stdsrc.addstr(y, x, option)

        # Get input
        key = stdsrc.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1

        elif key == curses.KEY_DOWN and selected < len(options) - 1:
            selected += 1

        # When the enter key is pressed check the selected option
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Exit the loop
            if options[selected] == 'Start Typing':
                break

            # Quit the program
            elif options[selected] == 'Exit':
                quit()


def game(stdsrc):
    '''
    Let's you play the game
    '''

    global minutes, wpm

    sentence = get_quote()
    user_input = ''

    # Get the time when the game starts
    start = time.time()

    while True:
        # Clear screen
        stdsrc.clear()
        
        # Check if the user has typed all the sentence
        if user_input == sentence:
            break

        # Check every letter of the sentence and of the user input
        for i in range(len(sentence)):

            # While the user has written something
            if i < len(user_input):
                current = user_input[i]
                
                # If it's correct then print it as green
                if current == sentence[i]:
                    stdsrc.addstr(current, curses.color_pair(1))

                # If it's wrong then print it as red
                else:
                    stdsrc.addstr(current, curses.color_pair(2))

            # Else if the user didn't typed until now
            else:
                # If it's the letter the user is about to type then highlight it
                if i == len(user_input):
                    stdsrc.addstr(sentence[i], curses.color_pair(3))

                # Else print it normally
                else:
                     stdsrc.addstr(sentence[i])

        # Get input as string
        key = stdsrc.getkey()

        # If the user pressed the backspace then delete the last letter
        if key == 'KEY_BACKSPACE':
            user_input = user_input[:-1]

        # Else if it's a valid key, add it to the user input
        elif key in VALIDS:
            user_input += key

        # Refresh the screen to see the changes
        stdsrc.refresh()

    # Get the time when the game ends
    stop = time.time()

    # Calculate the minutes by subtracting the final and the initial time, dividing by 60 and rounding to the seconds
    minutes = round((stop - start) / 60, 2)

    # Calculate the WPM, see: https://www.speedtypingonline.com/typing-equations
    wpm = round((len(sentence) / 5) / minutes)


def score(stdsrc):
    '''
    Display the score
    '''

    global minutes, wpm

    # Clear the screen
    stdsrc.clear()

    # Get width and height
    height, width = stdsrc.getmaxyx()
    
    # Calculate the y (should be the center of the screen)
    y = height // 2

    # Center all the elements

    minutes_string = 'Time (minutes): ' + str(minutes)
    x = width // 2 - len(minutes_string) // 2
    stdsrc.addstr(y - 3, x, minutes_string)

    wpm_string = 'WPM: ' + str(wpm)
    x = width // 2 - len(wpm_string) // 2
    stdsrc.addstr(y - 2, x, wpm_string)

    message = 'Press any key to continue'

    x = width // 2 - len(message) // 2
    stdsrc.addstr(y + 1, x, message)

    # Wait for a key
    stdsrc.getch()


def main(stdsrc):
    '''
    Define the main loop of the application
    '''

    # Set cursor as invisible
    curses.curs_set(0)

    # Initialize color schemes
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Main loop
    while True:
        menu(stdsrc)
        game(stdsrc)
        score(stdsrc)


curses.wrapper(main)

