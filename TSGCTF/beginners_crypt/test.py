assert(len(open('flag.txt', 'rb').read()) <= 50)

plain = int.from_bytes(open('flag.txt', 'rb').read(), byteorder='big')
left_shift = int.from_bytes(open('flag.txt', 'rb').read(), byteorder='big') << 10000
left_right_shift = left_shift >> 10000

num = 2 ** 10000

print("left 10000 shifted : " + str(left_shift))
print("plain : " + str(plain))
print("left 10000 => right 10000 shifted : " + str(left_right_shift))
print(left_right_shift.to_bytes(32, 'big'))

print(str(num))
