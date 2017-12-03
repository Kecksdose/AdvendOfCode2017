import itertools as it
import math as m

def get_distance_from_center(n):
    # Easy case
    if n == 1:
        return 0

    # Toggle directions
    directions = it.cycle([
        (+1, 0),  # right
        (0, +1),  # up
        (-1, 0),  # left
        (0, -1)   # down
    ])
    cur_direction = next(directions)

    vals_and_positions = {}
    vals_and_positions[1] = (0, 0)

    # How to build a spiral:
    # 1 right, 1 up, 2 left, 2 down, 3 right, 3 up, 4 left, 4 down...
    # These values are always lower than the sqrt of the highest value in the
    # spiral.
    sequence_done_one_time = True  # Because val 1 was already set
    # +2, because better save than sorry
    steps_per_direction = list(range(1, m.floor(m.sqrt(n)) + 2))
    steps_per_direction_position = 0
    n_steps_to_go_in_direction = 1

    for i in range(2, n + 1):
        vals_and_positions[i] = (
            vals_and_positions[i-1][0] + cur_direction[0],
            vals_and_positions[i-1][1] + cur_direction[1]
        )
        n_steps_to_go_in_direction -= 1

        if n_steps_to_go_in_direction == 0:

            if sequence_done_one_time:
                n_steps_to_go_in_direction = steps_per_direction[
                    steps_per_direction_position
                ]
                steps_per_direction_position += 1
            else:
                n_steps_to_go_in_direction = steps_per_direction[
                    steps_per_direction_position
                ]
            sequence_done_one_time = not sequence_done_one_time
            cur_direction = next(directions)

    distance = abs(vals_and_positions[n][0]) + abs(vals_and_positions[n][1])
    return distance


def solve(file):
    with open(file, 'r') as f:
        number = f.read()
        number = number.rstrip('\n')
        number = int(number)

        return get_distance_from_center(number)

# # Test examples
files_and_solutions = {
    'test1.txt': 0,
    'test2.txt': 3,
    'test3.txt': 2,
    'test4.txt': 31
}

for file, solution in files_and_solutions.items():
    assert solve(file) == solution

# Solve riddle
print(solve('riddle.txt'))
