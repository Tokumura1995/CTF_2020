#!/usr/bin/env python3
from base64 import b64decode
import blacklist  # you don't get to see this :p

"""
Don't worry, if you break out of this one, we have another one underneath so that you won't
wreak any havoc!
"""

def main():
    print("EduPy 3.8.2")
    while True:
        try:
            command = input(">>> ")
            if any([x in command for x in blacklist.BLACKLIST]):
                raise Exception("not allowed!!")

            final_cmd = """
fd = open("sandbox.py", "r")
offset = 1
readline = fd.readlines()[offset].strip().split(" ")
AA = readline[offset]
AA_rev = readline[-offset]
fd.close()
Hr = getattr(__import__(AA), AA_rev)
RMbPOQHCzt = __builtins__.__dict__[Hr(b'X19pbXBvcnRfXw==').decode('utf-8')](Hr(b'bnVtcHk=').decode('utf-8'))\n""" + command
            exec(final_cmd)

        except (KeyboardInterrupt, EOFError):
            return 0
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    exit(main())
