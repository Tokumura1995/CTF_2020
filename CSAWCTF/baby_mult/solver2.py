from pwn import *

def main():
    code = b""
    with open("program.txt", "r") as f_1:
        for c in f_1.readline().split(", "):
            code += struct.pack("B", int(c))
    
    print(disasm(code, arch = 'amd64'))    

if __name__ == "__main__":
    main()