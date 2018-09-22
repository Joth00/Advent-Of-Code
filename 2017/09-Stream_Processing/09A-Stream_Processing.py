mystream = open('stream.txt', 'r').read().replace('\n', '')
stream = list(mystream)

lvl = 0
score = 0
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
        if crnt == '{':
            lvl += 1
            score += lvl
        elif crnt == '}':
            lvl -= 1
        elif crnt == '<':
            garbage = True
    x += 1

print('score:', score)
