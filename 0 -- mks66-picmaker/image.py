#picmaker

file = open('image.ppm', 'w')

def header():
    file.write('P3\n')
    file.write('500 500\n')
    file.write('255\n')

def picture():
    for y in range(500):
        for x in range(500):
            r = str((y / 2) % 255) + ' '
            g = str((x / (y + 1) * x) % 255) + ' '
            b = str((y / (x + 1) * y) % 255) + ' '
            file.write(r + g + b + '\t')
        file.write('\n')

header()
picture()
