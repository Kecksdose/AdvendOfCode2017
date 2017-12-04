import itertools as it
import math as m

def get_next_squared_number(n):
    # Easy case
    if n == 1:
        return 1

    # Toggle directions
    directions = it.cycle([
        (+1, 0),  # right
        (0, +1),  # up
        (-1, 0),  # left
        (0, -1)   # down
    ])
    neighbors = [
        (+1, 0),  # right
        (+1, +1), # up right
        (0, +1),  # up
        (-1, +1), # up left
        (-1, 0),  # left
        (-1, -1), # down left
        (0, -1),  # down
        (+1, -1)  # down richt
    ]
    cur_direction = next(directions)

    positions_and_vals = {}
    cur_position = (0, 0)
    positions_and_vals[cur_position] = 1

    # How to build a spiral:
    # 1 right, 1 up, 2 left, 2 down, 3 right, 3 up, 4 left, 4 down...
    # These values are always lower than the sqrt of the highest value in the
    # spiral.
    sequence_done_one_time = True  # Because val 1 was already set
    # +2, because better save than sorry
    steps_per_direction = list(range(1, m.floor(m.sqrt(n)) + 2))
    steps_per_direction_position = 0
    n_steps_to_go_in_direction = 1
    cur_val = 1

    def sum_over_all_existing_neighbors(
        cur_position,
        positions_and_vals=positions_and_vals,
        neighbors=neighbors
    ):
        val = 0
        for neighbor in neighbors:
            val += positions_and_vals.get((
                cur_position[0] + neighbor[0],
                cur_position[1] + neighbor[1]
            ), 0)
        return val

    for i in range(2, n + 100):  # Should be enough :D
        if cur_val <= n:
            cur_position = (
                cur_position[0] + cur_direction[0],
                cur_position[1] + cur_direction[1]
            )
            cur_val = sum_over_all_existing_neighbors(
                cur_position
            )
            positions_and_vals[cur_position] = cur_val
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
        else:
            return cur_val


def solve(file):
    with open(file, 'r') as f:
        number = f.read()
        number = number.rstrip('\n')
        number = int(number)

        return get_next_squared_number(number)

# Test examples
### No real tests on this riddle

# # Solve riddle
print(solve('riddle.txt'))
