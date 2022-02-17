import random
import mirrorselect
import os

def huboptions():
    print('[0] Exit')
    print('[1] Select Mirrors')
    print('[2] 2')

huboptions()
hubmenu = input('Input: ')
while hubmenu != '0':
    if int(hubmenu) == 1:
        print('1')
        mirrorselect.locatemirrors()
    elif int(hubmenu) == 2:
        print('2')
    else:
        print('invalid input')
    huboptions()
    hubmenu = input('Input: ')
print('Closing program')
exit()
