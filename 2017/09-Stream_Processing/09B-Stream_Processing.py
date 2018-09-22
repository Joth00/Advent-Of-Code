mystream = open('stream.txt', 'r').read().replace('\n', '')
stream = list(mystream)

removed = 0
garbage = False
x = 0
while x < len(stream):
    crnt = stream[x]
    if garbage == True:
        if crnt == '!':
            x += 1
        elif crnt == '>':
            garbage = False
        else:
            removed += 1
    else:
        if crnt == '<':
            garbage = True
    x += 1

print('removed garbage:', removed)
