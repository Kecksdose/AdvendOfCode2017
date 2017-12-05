def solve(file):
    with open(file, 'r') as f:
        numbers = []
        for line in f.readlines():
            numbers.append(int(line))
        n_steps = 0
        cur_position = 0
        while True:
            try:
                prev_position = cur_position
                distance = numbers[cur_position]
                cur_position += distance
                if distance >= 3:
                    numbers[prev_position] -= 1
                else:
                    numbers[prev_position] += 1
                n_steps += 1
            except:
                return n_steps


# Test examples
assert solve('test.txt') == 10


# Solve riddle
print(solve('riddle.txt'))

