def solve(file):
    with open(file) as f:
        checksum = 0
        for line in f:
            # Remove endline
            line = line.rstrip('\n')
            line = line.split()
            line = [int(num) for num in line]
            min_val = min(line)
            max_val = max(line)
            diff = max_val - min_val
            checksum += diff

        return checksum

# Test example
assert solve('test.txt') == 18

# Solve riddle
print(solve('riddle.txt'))
