# Many thanks to https://www.redblobgames.com/grids/hexagons/#distances

def solve(file):
    with open(file, 'r') as f:
        instructions = f.read()
        instructions = instructions.strip('\n')
        instructions = instructions.split(',')

        directions = {
            'n':  (+1, -1,  0),
            'ne': (+1,  0, -1),
            'se': ( 0, +1, -1),
            's':  (-1, +1,  0),
            'sw': (-1,  0, +1),
            'nw': ( 0, -1, +1)
        }

        cur_position = (0, 0, 0)
        for instruction in instructions:
            cur_position = (
                cur_position[0] + directions[instruction][0],
                cur_position[1] + directions[instruction][1],
                cur_position[2] + directions[instruction][2]
            )

        # Return shortest distance
        return max(
            abs(cur_position[0]),
            abs(cur_position[1]),
            abs(cur_position[2])
        )


# Test examples
files_and_solutions = {
    'test1.txt': 3,
    'test2.txt': 0,
    'test3.txt': 2,
    'test4.txt': 3
}

for file, solution in files_and_solutions.items():
    assert solve(file) == solution


# Solve riddle
print(solve('riddle.txt'))

