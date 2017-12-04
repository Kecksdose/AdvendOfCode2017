def solve(file):
    with open(file, 'r') as f:
        content = f.read()
        content = content.rstrip('\n')

        n_digits = len(content)
        n_digits_half = int(n_digits/2)

        total = 0

        for i in range(0, n_digits_half):
            if content[i] == content[n_digits_half + i]:
                total += int(content[i])

        # The second half should be the same --> Two times total
        return total * 2

# Test examples
files_and_solutions = {
    'test1.txt': 6,
    'test2.txt': 0,
    'test3.txt': 4,
    'test4.txt': 12,
    'test5.txt': 4,
}

for file, solution in files_and_solutions.items():
    assert solve(file) == solution

# Solve riddle
print(solve('riddle.txt'))
