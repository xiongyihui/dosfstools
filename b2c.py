#!/usr/bin/env python

import sys
import string

def bin2array(binary, output):
    b = file(binary, 'rb')
    o = file(output, 'wt')

    o.write('const unsigned char DiskImage[] = {\n')

    count = 0
    while True:
        byte = b.read(1)
        if len(byte) != 1:
            break

        o.write('0x%02x,' % ord(byte))

        count = count + 1
        if count == 16:
            count = 0
            o.write('\n')

    if count == 0:
        o.write('};\n')
    else:
        o.write('\n};\n')

    b.close()
    o.close()

if __name__ == '__main__':
    try:
        bin2array(sys.argv[1], sys.argv[2])
    except IndexError:
        print 'Usage: %s binary output' % sys.argv[0]
        raise SystemExit



