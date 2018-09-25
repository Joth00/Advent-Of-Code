def check(a, b):
    if a == b:
        result = False
    elif len(a) == len(b) == 1:
        result = None
    elif len(a) == len(b) == 2:
        if a[0] != b[0] and a[1] != b[1]:
            result = None
        elif a[0] == b[0]:
            result = a[0]
        elif a[1] == b[1]:
            result = False
    elif len(a) != len(b):
        if a[0] == b[0]:
            result = False
        elif len(a) == 1:
            result = a + b[1]
        elif len(b) == 1:
            result = b + a[1]
    return result


inpt = open('directions.txt', 'r').read().replace('\n', '')
rawdirs = inpt.split(',')
tot = len(rawdirs)
lengths = list()

for y in range(1, len(rawdirs)):
    dirs = rawdirs[:y]
    print('#', y, '/', tot)
    for x in range(len(dirs)):
        for i in [a for a in range(len(dirs)-1) if a != x]:
            if dirs[x] == None or dirs[i] == None:
                continue
            checked = check(dirs[x], dirs[i])
            if checked != False:
                dirs[i] = checked
                dirs[x] = None
                break
    dirs = list(filter(None, dirs))
    lengths.append(len(dirs))

maxdistance = max(lengths)

print(dirs)
print('Max distance:', maxdistance)