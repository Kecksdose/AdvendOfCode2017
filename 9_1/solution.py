def solve(file):
    with open(file, 'r') as f:
        group_level = 0
        is_garbage = False
        skip_next = False
        garbage_counter = 0

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

                else:
                    garbage_counter += 1
            # At last, check for other chars
            else:
                if char == '<':
                    is_garbage = True
                    continue
                elif char == '{':
                    group_level += 1
                    continue
                elif char == '}':
                    group_level -= 1
                    continue
                elif char == '!':
                    skip_next = True
                    continue
                else:
                    continue

        return garbage_counter

# Test examples
files_and_solutions = {
    'test1.txt': 0,
    'test2.txt': 17,
    'test3.txt': 3,
    'test4.txt': 2,
    'test5.txt': 0,
    'test6.txt': 0,
    'test7.txt': 10,
}
for file, solution in files_and_solutions.items():
    assert solve(file) == solution


# Solve riddle
print(solve('riddle.txt'))

