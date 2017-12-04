def solve(file):
    with open(file) as f:
        checksum = 0
        for line in f:
            # Remove endline
            line = line.rstrip('\n')
            line = line.split()
            line = [int(num) for num in line]
            small_to_great = sorted(line)
            great_to_small = small_to_great[::-1]

            # One could improve performance here
            for val1 in great_to_small:
                for val2 in small_to_great:
                    if val1%val2 == 0 and val1 != val2:
                        checksum += int(val1/val2)

        return checksum

# Test example
assert solve('test.txt') == 9

# Solve riddle
print(solve('riddle.txt'))
