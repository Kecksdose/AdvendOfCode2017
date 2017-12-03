def solve(file):
    with open(file, 'r') as f:
        content = f.read()
        content = line.rstrip('\n')

        prev_val = 0
        total = 0
        for val in content:
            val = int(val)
            if val == prev_val:
                total += val

            prev_val = val

        # Check also first and last
        if content[0] == content[-1]:
            total += int(content[0])

        return total

# Test examples
files_and_solutions = {
    'test1.txt': 3,
    'test2.txt': 4,
    'test3.txt': 0,
    'test4.txt': 9
}

for file, solution in files_and_solutions.items():
    assert solve(file) == solution

# Solve riddle
print(solve('riddle.txt'))
