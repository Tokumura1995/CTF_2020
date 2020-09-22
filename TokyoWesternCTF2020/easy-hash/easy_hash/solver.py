import struct
import os   

MSG = b'twctf: please give me the flag of 2020'

def easy_hash(x):
    m = 0
    for i in range(len(x) - 3):
        print(x[i: i + 4])
        m += struct.unpack('<I', x[i:i + 4])[0]
        m = m & 0xffffffff
    return m

def main():
    expected_hash = easy_hash(MSG)
    print(expected_hash)


if __name__ == "__main__":
    main()