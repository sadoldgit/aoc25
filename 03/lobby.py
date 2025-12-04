def part1(banks):
    total_joltage = 0
    for bank in banks:
        maxj = '00'
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                if bank[i]+bank[j] > maxj:
                    maxj = bank[i]+bank[j]
        total_joltage += int(maxj)
    return total_joltage


def part2(banks):
    total_joltage = 0
    for bank in banks:
        blen = len(bank)
        searchstart = 0
        batjoltages = ['0'] * 12
        for battery in range(12):
            # to have the largest digit on the next place, exhaust
            # until there's no more room for the following digits
            for i in range(searchstart, blen - 11 + battery):
                if bank[i] > batjoltages[battery]:
                    batjoltages[battery] = bank[i]
                    searchstart = i + 1
                if batjoltages[battery] == '9':
                    break
        joltage = int(''.join(batjoltages))
        total_joltage += joltage
    return total_joltage


# ...relax time: https://www.youtube.com/shorts/Gp3sFLRcIY0
           
def main():
    banks = []
    for bank in open('input.txt').readlines():
        banks.append([bat for bat in bank.strip()])
    print(f'Part 1 {part1(banks)}')
    print(f'Part 2 {part2(banks)}')


if __name__ == '__main__':
    main()