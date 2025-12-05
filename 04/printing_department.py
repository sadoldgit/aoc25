class Map:
    
    def __init__(self, fname):
        self.map = []
        for row in open(fname).readlines():
            self.map.append([pos for pos in row.strip()])
        self.height = len(self.map)
        self.width  = len(self.map[0])
        self._nhood = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1),
                       (1, -1), (1, 0), (1, 1)]

    def neighbors(self, row, col):
        for n in self._nhood:
            r, c = row + n[0], col + n[1]
            if r >= 0 and r < self.height and c >= 0 and c < self.width:
                yield (r, c)
                
    def __iter__(self):
        for r in range(self.height):
            for c in range(self.width):
                yield (r, c, self.map[r][c])
                

def part1(rolls: Map):
    for row, col, obj in rolls:
        if obj == '@':
            ncnt = 0
            for nr, nc in rolls.neighbors(row, col):
                ncnt += 1 if rolls.map[nr][nc] == '@' else 0
            if ncnt < 4:
                yield (row, col)


def part2(rolls: Map):
    removed_cnt = 0
    remove = [roll for roll in part1(rolls)]
    while len(remove) > 0:
        for row, col in remove:
            rolls.map[row][col] = '.'
        removed_cnt += len(remove)
        remove = [roll for roll in part1(rolls)]
    return removed_cnt


# ...relax time: https://www.youtube.com/shorts/n863sO9jsYY


def main():
    rolls = Map('input.txt')
    print(f'Part 1 {sum(1 for _ in part1(rolls))}')
    print(f'Part 2 {part2(rolls)}')


if __name__ == '__main__':
    main()