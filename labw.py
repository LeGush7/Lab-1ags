# задание №1
inputheight = int(input('Введите высоту флага: '))
heightcolour = (inputheight + 1) // 3 if inputheight > 2 else 1
for i in range(heightcolour):
    print('\x1b[48;2;250;185;0m ' * int((heightcolour // 0.1)), '\x1b[0m')
for i in range(heightcolour):
    print('\x1b[48;2;9;101;64m ' * int((heightcolour // 0.1)), '\x1b[0m')
for i in range(heightcolour):
    print('\x1b[48;2;190;42;42m ' * int((heightcolour // 0.1)), '\x1b[0m')

# задание №2
STARTLENGTH = 7
height = STARTLENGTH + 1
filledcells = STARTLENGTH - 1
emptycells = 0
numsoffcells = [int(x - 1) for x in range(STARTLENGTH + 1, 2, -1)]
print(STARTLENGTH * '\x1b[48;5;27;1m \x1b[0m' + (sum(numsoffcells) * 2
     - STARTLENGTH * 2 + 1) * ' ' +
     STARTLENGTH * '\x1b[48;5;27;1m \x1b[0m')
for h in range(height):
    if filledcells != 1:
        emptycells += 1
        print(' ' * sum(numsoffcells[0:emptycells]) +
              '\x1b[48;5;27;1m \x1b[0m' * numsoffcells[emptycells] +
              (sum(numsoffcells) * 2 - (sum(numsoffcells[0:emptycells +
              1])) * 2 + 1) * ' ' + '\x1b[48;5;27;1m \x1b[0m' *
              numsoffcells[emptycells] +
              ' ' * sum(numsoffcells[0:emptycells]))
        filledcells -= 1
    else:
        print((sum(numsoffcells)) * ' ' +
              '\x1b[48;5;27;1m \x1b[0m' + (sum(numsoffcells)) * ' ')

# задание №3
HEIGTH = 9
WIDTH = 9
lastcells = 1
for y in range(HEIGTH):
    print((WIDTH - lastcells) * ' ' + '\x1b[48;5;27;1m \x1b[0m')
    lastcells += 1

# задание №4
with open("sequence.txt") as sequence:
    data = sequence.read()
valueslist = [abs(float(num)) for num in data.split('\n')]
oddvalue, notoddvalue = 0, 0
for i in range(0, len(valueslist), 2):
    notoddvalue += valueslist[i]
for i in range(1, len(valueslist), 2):
    oddvalue += valueslist[i]
allvalues = oddvalue + notoddvalue
procentodd = round((oddvalue / allvalues) * 100)
procentnotodd = round((notoddvalue / allvalues) * 100)
print('Нечёт. позиции', '\x1b[48;5;27;10m ' * procentodd, '\x1b[0m')
print('Чёт. позиции  ', '\x1b[48;5;27;10m ' * procentnotodd, '\x1b[0m')
