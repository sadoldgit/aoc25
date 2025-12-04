def part1(id_ranges):
    sum_invalid = 0
    for id_range in id_ranges:
        for prod_id in range(int(id_range[0]), int(id_range[1]) + 1):
            idstr = str(prod_id)
            idlen = len(idstr)
            if idlen % 2 == 0 and idstr[:idlen//2] == idstr[idlen//2:]:
                sum_invalid += prod_id
    return sum_invalid


def part2(id_ranges):
    sum_invalid = 0
    for id_range in id_ranges:
        for prod_id in range(int(id_range[0]), int(id_range[1]) + 1):
            idstr = str(prod_id)
            idlen = len(idstr)
            myids = set() # e.g, 222222: "22"*3 | "222"*2, count only once
            for i in range(1, idlen // 2 + 1):
                if not idlen % i == 0:
                    continue
                nrparts = idlen // i
                if idstr[:i] * nrparts == idstr and not idstr in myids:
                    sum_invalid += prod_id
                    myids.add(idstr)
    return sum_invalid


# ...relax time: https://www.youtube.com/watch?v=_rECIcx3S68&list=RDYOn8tuqCTA8&index=2


def main():
    id_ranges = open('input.txt').read().strip().split(',')
    id_ranges = [id_range.split('-') for id_range in id_ranges]
    print(f'Part 1 {part1(id_ranges)}')
    print(f'Part 2 {part2(id_ranges)}')


if __name__ == '__main__':
    main()
