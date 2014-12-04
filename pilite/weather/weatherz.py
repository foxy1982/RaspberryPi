#!/usr/bin/env python

import sys
sys.path.append('/home/pi/git/PiLite/Python_Examples')

from PiLiteLib import PiLiteBoard

def main():
    for x in range (0,10):
        sink = PiLiteBoard()
        print ("This is the time %d" % (x)) 
        sink.write("This is ths asd asd asd asd asd asd asd This is the time: %d" % (x))

if __name__ == "__main__":
    main()

