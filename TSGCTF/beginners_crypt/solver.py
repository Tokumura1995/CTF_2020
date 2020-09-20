num = 2 ** 10000
print(str(num)[-175:])

endwith_int = 1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576

endwith_str = str(endwith_int)

div_num_array = []
for i in range(175):
    print(i)
    for j in range(10):
        mul_num_str = ""
        for i in div_num_array:
            mul_num_str = str(i) + mul_num_str
        mul_num = int(str(j) + mul_num_str)
        print("mulnum : " + str(mul_num))

        if (str(num * mul_num)[(i + 1) * (-1)] != endwith_str[(i + 1) * (-1)]):
            continue
        else:
            for k in range(10):
                mul_num = int(str(k) + str(j))
                if (str(num * mul_num)[(i + 1) * (-1) - 1:(i + 1) * (-1)] != endwith_str[(i + 1) * (-1) - 1:(i + 1) * (-1)]):
                    continue

            if k == 9 and (str(num * mul_num)[(i + 1) * (-1) - 1:(i + 1) * (-1)] != endwith_str[(i + 1) * (-1) - 1:(i + 1) * (-1)]):
                continue
            else:
                break

    div_num_array.append(j)

ans_str = ""
for i in reversed(div_num_array):
    ans_str += str(i)

print(ans_str)
print(int(ans_str).to_bytes(1024, 'big'))
