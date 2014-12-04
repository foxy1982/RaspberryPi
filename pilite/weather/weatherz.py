#!/usr/bin/env python

import sys
sys.path.append('/home/pi/git/PiLite/Python_Examples')

from PiLiteLib import PiLiteBoard

def main():
    sink = PiLiteBoard()
    print ("ready")
    sink.write("Hello")

if __name__ == "__main__":
    main()

