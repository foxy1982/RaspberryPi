#!/usr/bin/env python

from PiLiteLib import PiLiteBoard

def main():
    sink = PiLiteBoard()
    print ("ready")
    sink.write("Hello")

if __name__ == "__main__":
    main()

