S=0 # range start
E=1 # range end

class Inventory:
    
    def __init__(self, dbfile):
        self.freshranges = []
        self.ingredients = []
        with open(dbfile) as f:
            for line in f.readlines():
                line = line.rstrip()
                if '-' in line:
                    idfrom, idto = line.split('-')
                    self.freshranges.append((int(idfrom), int(idto)))
                elif line == '':
                    continue
                else:
                    self.ingredients.append(int(line))
        self.freshranges = sorted(self.freshranges)
    
    def is_fresh(self, iid):
        for ffrom, fto in self.freshranges:
            if iid >= ffrom and iid <= fto:
                return True
        return False
    
    def disjunct_ranges(self):
        # note: sorted freshranges list is expected
        # (each next has starting point after the starting point of previous)
        last = self.freshranges[0]
        for cur in self.freshranges[1:]:
            if cur[S] <= last[E]: # current range starts within last
                if cur[E] < last[E]:
                    continue # new range is (fully) within last
                else: # merge into one
                    last = (last[S], cur[E])
            else: # current starts after last but also not immediately
                yield last
                last = cur
        yield last


def part1(inv: Inventory):
    return sum([1 if inv.is_fresh(iid) else 0 for iid in inv.ingredients])


def part2(inv: Inventory):
    return sum([rng[E] - rng[S] + 1 for rng in inv.disjunct_ranges()])


# ...relax time: https://www.youtube.com/watch?v=iK1QRjduxps


def main():
    inventory = Inventory('input.txt')
    print(f'Part 1 {part1(inventory)}')
    print(f'Part 2 {part2(inventory)}')


if __name__ == '__main__':
    main()