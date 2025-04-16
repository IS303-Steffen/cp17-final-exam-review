'''
I add a reference to this function in all the practice files just because
it increases the viewable screen area when following along in class
'''

import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')