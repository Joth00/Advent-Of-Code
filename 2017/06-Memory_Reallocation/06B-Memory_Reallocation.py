my_input = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'

banks = list(map(int, my_input.split()))
history = []
steps = 0

while banks not in history[:-1]:
    steps += 1
    val = max(banks)
    pos = banks.index(val)
    banks[pos] = 0

    while val != 0:
        if pos == len(banks) - 1:
            pos = 0
        else:
            pos += 1
        banks[pos] += 1
        val -= 1

    history.append(banks[:])

cycles = len(history) - 1 - history.index(banks)
temp = list(map(str, banks))
print("'%s' is seen again after %d cycles." % (' '.join(temp), cycles))
