.PHONY: clean all sudo

all: hello stage1 stage2 stage3 stage4

hello: hello.asm hihi.asm hello-asm hello.c
	nasm -f elf64 hello.asm
	ld -s -o hello-asm hello.o
	nasm -f elf64 hihi.asm
	ld -s -o hihi-asm hihi.o
	gcc -Wall -o hello-c hello.c
	gcc -Wall -static -o hello-static hello.c

stage1: stage1.c
	gcc -Wall -m32 -o stage1 stage1.c
	gcc -Wall -m32 -fno-stack-protector -no-pie -o stage1_noprot stage1.c
	gcc -Wall -m32 -fstack-protector-all -no-pie -o stage1_protectorall stage1.c
	gcc -Wall -m32 -fno-stack-protector -no-pie -g -o stage1_debug stage1.c

stage2: stage2.c
	gcc -Wall -m32 -fno-stack-protector -z execstack -no-pie -o stage2 stage2.c

stage3: stage3.c
	gcc -Wall -m32 -fno-stack-protector -no-pie -o stage3 stage3.c

stage4: stage4.c
	gcc -Wall -m32 -fno-stack-protector -o stage4 stage4.c
	gcc -Wall -m32 -fno-stack-protector -no-pie -o stage4_nopie stage4.c

sudo:
	sudo chown root ./stage1 && sudo chmod u+s ./stage1

uaf: uaf.c
	gcc -Wall -m32 -fno-stack-protector -no-pie -o uaf uaf.c

clean:
	rm stage1 stage2 stage3 stage1_protectorall
