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

def main():
    bin_str = ""
    print(target.recvline())
    for i in range(176):
        print("[*]round {}".format(i))
        print(target.recvline())
        target.sendline(b"A" * 32)
        print(target.recvuntil("Ciphertext is:  "))
        cipher_text = target.recvline()[:-1]
        print(cipher_text)
        print(target.recvline())
        if cipher_text[0:16] in cipher_text[16:]:
            target.sendline("ECB")
            print(" [+]ECB")
            bin_str += "0"
        else:
            target.sendline("CBC")
            print(" [+]CBC")
            bin_str += "1"

    print(int(bin_str, 2).to_bytes(32, 'big'))


if __name__ == "__main__":
    main()