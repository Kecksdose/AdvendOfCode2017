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

        def get_shortest_distance(cur_position):
            return max(
                abs(cur_position[0]),
                abs(cur_position[1]),
                abs(cur_position[2])
            )

        cur_position = (0, 0, 0)
        longest_distance = 0

        for instruction in instructions:
            cur_position = (
                cur_position[0] + directions[instruction][0],
                cur_position[1] + directions[instruction][1],
                cur_position[2] + directions[instruction][2]
            )
            distance = get_shortest_distance(cur_position)
            if distance > longest_distance:
                longest_distance = distance

        # Return longest distance
        return longest_distance


# Test examples
# No real examples here :(


# Solve riddle
print(solve('riddle.txt'))

