def solve(file):
    with open(file, 'r') as f:
        group_level = 0
        is_garbage = False
        skip_next = False
        total_score = 0

        input = f.read()
        for char in input:
            # Most important: skip
            if skip_next:
                skip_next = False
                continue

            # Then check if in garbage
            if is_garbage:
                if char == '!':
                    skip_next = True
                    continue

                elif char == '>':
                    is_garbage = False
                    continue
            # At last, check for other chars
            else:
                if char == '<':
                    is_garbage = True
                    continue
                elif char == '{':
                    group_level += 1
                    continue
                elif char == '}':
                    total_score += group_level
                    group_level -= 1
                    continue
                elif char == '!':
                    skip_next = True
                    continue
                else:
                    continue

        return total_score

# Test examples
files_and_solutions = {
    'test1.txt': 1,
    'test2.txt': 6,
    'test3.txt': 5,
    'test4.txt': 16,
    'test5.txt': 1,
    'test6.txt': 9,
    'test7.txt': 9,
    'test8.txt': 3
}
for file, solution in files_and_solutions.items():
    assert solve(file) == solution


# Solve riddle
print(solve('riddle.txt'))

