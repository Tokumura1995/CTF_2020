import ctypes
import struct

def main():
    code = b""
    with open("program.txt", "r") as f_1:
        for c in f_1.readline().split(", "):
            code += struct.pack("B", int(c))
    
    libc = ctypes.CDLL('/lib/x86_64-linux-gnu/libc.so.6')
    sc_ptr = ctypes.c_char_p(code)
 
    size = len(code)
    addr_aligned = ctypes.c_void_p(libc.valloc(size))
    ctypes.memmove(addr_aligned, sc_ptr, size)
    libc.mprotect(addr_aligned, size, 1 | 2 | 4) 
 
    func = ctypes.cast(addr_aligned, ctypes.CFUNCTYPE(ctypes.c_void_p))
    func()

if __name__ == "__main__":
    main()