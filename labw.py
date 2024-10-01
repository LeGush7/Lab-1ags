# задание №1
print('\x1b[48;2;250;185;0m            \x1b[0m')
print('\x1b[48;2;9;101;64m            \x1b[0m')
print('\x1b[48;2;190;42;42m   \x1b[38;2;190;42;42m         \x1b[0m')
# цельный пробел разделён на два, т.к. цельный не выводится; если уменьшить общую длинну, то нарушится пропорция 3:5

# задание №2
st = 7
height = st + 1
kz = st - 1
prob = 0
pr = [int(x - 1) for x in range(st + 1, 2, -1)]
print(st * '\x1b[48;5;27;1m \x1b[0m' + (sum(pr) * 2 - st * 2 + 1) * ' ' + st * '\x1b[48;5;27;1m \x1b[0m')
for h in range(height):
    if kz != 1:
        prob += 1
        print(' ' * sum(pr[0:prob]) + '\x1b[48;5;27;1m \x1b[0m' * pr[prob] + (sum(pr) * 2 -
                    (sum(pr[0:prob + 1])) * 2 + 1) * ' ' + '\x1b[48;5;27;1m \x1b[0m' * pr[prob] + ' ' * sum(pr[0:prob]))
        kz -= 1
    else:
        print((sum(pr)) * ' ' + '\x1b[48;5;27;1m \x1b[0m' + (sum(pr)) * ' ')

# задание №3
h, w = 9, 9
c = 1
for y in range(h):
    print((w - c) * ' ' + '\x1b[48;5;27;1m \x1b[0m')
    c += 1

# задание №4
import matplotlib.pyplot as p


vlist = [abs(float(x)) for x in open('sequence.txt')]
v1, v2 = 0, 0
for x in range(0, len(vlist), 2):
    v1 += vlist[x]
for x in range(1, len(vlist), 2):
    v2 += vlist[x]
v2 = round(v2, 1)
vs = [v1, v2]
nms = ['Чётные', 'Нечётные']
p.pie(vs, labels=nms, autopct=lambda p: '{:.2f}%'.format(p), startangle=90, colors=['#66ff66','#ffcc66'])
p.title('Процентное соотношение')
p.show()
