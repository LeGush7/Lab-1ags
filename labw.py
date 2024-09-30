print('\x1b[48;2;250;185;0m            \x1b[0m')
print('\x1b[48;2;9;101;64m            \x1b[0m')
print('\x1b[48;2;190;42;42m   \x1b[38;2;190;42;42m         \x1b[0m')


st = 7
height = st + 1
kz = st - 1
prob = 0
pr = [int(x - 1) for x in range(st + 1, 2, -1)]
print(st * '\x1b[48;5;27;1m \x1b[0m' + (sum(pr) * 2 - st * 2 + 1) * ' ' + st * '\x1b[48;5;27;1m \x1b[0m')
for h in range(height):
    if kz != 1:
        prob += 1
        print(' ' * sum(pr[0:prob]) + '\x1b[48;5;27;1m \x1b[0m' * pr[prob] + (sum(pr) * 2 - (sum(pr[0:prob + 1])) * 2 + 1) * ' ' + '\x1b[48;5;27;1m \x1b[0m' * pr[prob] + ' ' * sum(pr[0:prob]))
        kz -= 1
    else:
        print((sum(pr)) * ' ' + '\x1b[48;5;27;1m \x1b[0m' + (sum(pr)) * ' ')
# print("""
# ****           ****
#     ***     ***
#        ** **
#          *
#          *""")
h, w = 9, 9
c = 1
for y in range(h):
    print((w - c) * ' ' + '\x1b[48;5;27;1m \x1b[0m')
    c += 1

