def solve(file):
    with open(file, 'r') as f:
        n_valid = 0
        for line in f.readlines():
            line = line.split()
            # Sort word first to check for anagrams
            line = [''.join(sorted(word)) for word in line]
            if len(set(line)) < len(line):
                ### Invalid password
                pass
            else:
                ### Valid password
                n_valid += 1
        return n_valid


# Test examples
files_and_solutions = {
    'test1.txt': 1,  # Valid
    'test2.txt': 0,  # Invalid
    'test3.txt': 1,  # Valid
    'test4.txt': 1,  # Valid
    'test5.txt': 0,  # Invalid
}

for file, solution in files_and_solutions.items():
    assert solve(file) == solution


# Solve riddle
print(solve('riddle.txt'))

