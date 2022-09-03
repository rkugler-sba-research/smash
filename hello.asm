section .data
   hellotxt db 'this is the syscall' ; some text

section .text          ;Code Segment
   global _start

_start:
    mov	rax, 1		; system call number (sys_write)
    mov rdi, 2		; stdout
    mov rsi, hellotxt   ; text buffer buffer
    mov rdx, 20
    syscall		; call kernel

    mov rax, 60         ; exit system call
    xor rdi, rdi
    syscall
