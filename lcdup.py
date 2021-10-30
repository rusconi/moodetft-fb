#!/usr/bin/python3
#
#
# write datetime to file /home/pi/change.txt'
#

import os
import os.path
from os import path

from datetime import datetime

__version__ = "0.0.1"

filename = '/home/pi/change.txt'

def main():

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S - %d/%m/%Y")
    
    file = open(filename, 'w')
    
    file.write(current_time)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
