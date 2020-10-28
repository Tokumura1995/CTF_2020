f = lambda x : x
type_code = type(f.func_code)

consts = ("Hello, world!", None)
args = ("s",)

fake_code = b""
fake_code += b"\x64" + b"\x00\x00" # load_const
fake_code += b"\x47"              # print_item
fake_code += b"\x48"              # print_newline
fake_code += b"\x7c" + b"\x00\x00" # load_fast
fake_code += b"\x47"              # print_item
fake_code += b"\x48"              # print_newline
fake_code += b"\x64" + b"\x00\x01" # load_const
fake_code += b"\x53"              # return value

print(type(f.func_code))

f.func_code = type_code(
    1,           # argcount      
    1,           # nlocals
    1,           # stacksize
    67,          # flags
    fake_code,   # bytecode
    consts,      # constants
    (),          # local variables
    args,        # arguments
    "paooon.py", # filename
    "paooon_func", # objet name
    114514,      # line number
    "?"          # nazo
)


f("ponponmaru")
