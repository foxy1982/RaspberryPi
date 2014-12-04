#!/usr/bin/env python

import sys
sys.path.append('/home/pi/git/PiLite/Python_Examples')

from PiLiteLib import PiLiteBoard

def output(board, message):
   print(message)
   board.write(message)

def main():
    board = PiLiteBoard()
    for x in range (0,10):
        output (board, "This is the time %d" % (x)) 

if __name__ == "__main__":
    main()

