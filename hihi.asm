
section .text          ;Code Segment
   global _start

_start:
    mov	rax, 1		; sys_write system call
    mov rdi, 2		; stdout
    push 0x69486948     ; string "hihi"
    lea rsi, [rsp]      ; text buffer int argument 
    mov rdx, 4          ; length argument
    syscall

    mov rax, 60         ; exit system call
    xor rdi, rdi        ; return code
    syscall
