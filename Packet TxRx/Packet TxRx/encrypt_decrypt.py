#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import sys
import base64
import binascii

_debug = 0
state = 0
Pkt_len = 52

def custom_b64decode(s):
    try:
        return base64.b64decode(s)
    except binascii.Error:
        # Add padding characters and try again
        padding_length = (4 - len(s) % 4) % 4
        s += b'=' * padding_length
        return base64.b64decode(s)

if len(sys.argv) < 3:
    print('Usage: python3 encrypt_decrypt.py <input file> <output file>')
    print('Number of arguments=', len(sys.argv))
    print('Argument List:', str(sys.argv))
    exit(1)

fn = sys.argv[1]
if not os.path.exists(fn):
    print(fn, 'does not exist')
    exit(1)

f_in = open(fn, 'rb')

output_file = sys.argv[2]
f_out = open(output_file, 'wb')

while True:
    if state == 0:
        buff = f_in.read(Pkt_len)
        b_len = len(buff)
        if b_len == 0:
            print('End of file')
            break
        elif (buff[0] == 37) and (buff[51] == 93):
            continue
        else:
            # Use custom decoding function
            data = custom_b64decode(buff)
            f_out.write(data)
            if _debug:
                print("End of preamble")
            state = 1
    elif state == 1:
        buff = f_in.read(4)
        b_len = len(buff)
        if b_len == 0:
            print('End of file')
            break
        if buff[0] == 37:  # '%'
            if buff == b'%UUU':
                print("End of text")
                buff = f_in.read(4)  # Skip next four 'U's
                rcv_fn = []
                i = 0
                while i < 44:
                    ch = f_in.read(1)
                    if ch == b'%':
                        break
                    rcv_fn.append(ord(ch))
                    i += 1
                rf_len = len(rcv_fn)
                x = 0
                while x < rf_len:
                    rcv_fn[x] = chr(rcv_fn[x])
                    x += 1
                ofn = "".join(rcv_fn)
                print("Transmitted file name:", ofn)
                state = 2
                break
        else:
            # Use custom decoding function
            data = custom_b64decode(buff)
            f_out.write(data)
            continue

f_in.close()
f_out.close()

