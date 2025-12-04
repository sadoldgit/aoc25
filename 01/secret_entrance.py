def part1(moves):
    dial_pos = 50
    password = 0
    for move in moves:
# interesting facts:
# -1 % 100 = 99
# -100 % 100 = 0
        dial_pos = (dial_pos + move) % 100
        if dial_pos == 0:
            password += 1
    return password


def part2(moves):
    dial_pos = 50
    password = 0
    for move in moves:
# interesting facts:
# -1 // 100 = -1
# -100 // 100 = -1
# -101 // 100 = -2
# meaning, we could almost use the same for positive and negative:
        nr_zero_crossings = abs((dial_pos + move) // 100)
# yet:
        if move < 0:
# if we start from 0 (say move=-1, abs(-1//100) = 1), we'd immediately get +1
            if dial_pos == 0:
                nr_zero_crossings -= 1
# if we land on the 0, we'd miss one (due to 0//100 = 0)
            elif (dial_pos + move) % 100 == 0:
                nr_zero_crossings += 1
        password += nr_zero_crossings
        dial_pos = (dial_pos + move) % 100
    return password


# ...relax time: https://www.youtube.com/watch?v=YOn8tuqCTA8&list=RDYOn8tuqCTA8&start_radio=1


def main():
    lines = open('input.txt').readlines()
    moves = [(-1 if line[0] == 'L' else 1) * int(line[1:]) for line in lines]
    print(f'Part 1: {part1(moves)}')
    print(f'Part 2: {part2(moves)}')


if __name__ == '__main__':
    main()
