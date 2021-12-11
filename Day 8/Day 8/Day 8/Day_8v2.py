with open('../../Day-8-input.txt', 'r') as f:
    signals = [[set(i) for i in line.split()] for line in f.read().split('\n')]

def AOC_day8_pt1():
    total = 0
    for signal in signals:
        total += sum(len(digit) in (2, 3, 4, 7) for digit in signal[-4:])
    return total
    
def AOC_day8_pt2():
    total = 0
    for signal in signals:
        patterns = sorted(signal[:10], key=len)
        patterns[3:6] = sorted(patterns[3:6], key=lambda x: (patterns[1].issubset(x), len(patterns[2] & x)))
        patterns[6:9] = sorted(patterns[6:9], key=lambda x: (patterns[2].issubset(x), patterns[1].issubset(x)))
        patterns = [patterns[idx] for idx in (7, 0, 3, 5, 2, 4, 6, 1, 9, 8)]

        result = ''
        for digit in signal[-4:]:
            for idx, pattern in enumerate(patterns):
                if pattern == digit:
                    result += str(idx)
        total += int(result)
    return total

print(AOC_day8_pt1())
print(AOC_day8_pt2())