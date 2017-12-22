from itertools import cycle, count
import copy

class Scanner():
    def __init__(self, size=None):
        self.size = size
        self.cur_position = 0 if size else None

        self.cur_direction = 'down'

    def move(self):
        if not self.size:
            return

        if self.cur_direction == 'down':
            self.cur_position += 1
        elif self.cur_direction == 'up':
            self.cur_position -= 1

        if self.cur_position == self.size or self.cur_position == 0:
            self.toggle_direction()

    def toggle_direction(self):
        if self.cur_direction == 'up':
            self.cur_direction = 'down'
        elif self.cur_direction == 'down':
            self.cur_direction = 'up'

    def get_position(self):
        return self.cur_position

    def is_captured(self):
        return self.cur_position == 0

    def __repr__(self):
        return f'Scanner(size={self.size}, cur_position={self.cur_position})'

    def __deepcopy__(self, memodict={}):
        # This doesnt work ?!
        copy_scanner = Scanner(self.size)
        copy_scanner.cur_position = self.cur_position
        copy_scanner.cur_direction = self.cur_direction

        return copy_scanner

#@profile
def solve(file):
    # Really bad solution, takes 4s for 10k iterations :(. Maybe I have an idea
    # to speed this up in the next days
    with open(file, 'r') as f:
        # Read all instructions
        init_scanners = dict()

        for line in f.readlines():
            line = line.strip('\n')
            line = line.split(': ')
            line = [int(l) for l in line]
            init_scanners[line[0]] = Scanner(line[1] - 1)  # Start at 0

        # Fill empty depths, create scanners otherwise
        max_depth = max(init_scanners.keys())

        for i in range(max_depth + 1):
            if not i in init_scanners.keys():
                init_scanners[i] = Scanner()

        # Define move all scanner function
        def move_all(scanners):
            for scanner in scanners.values():
                scanner.move()
            return scanners

        # Save all scanner positions
        scanners_shifted_by = {0: init_scanners}

        def maybe_create_new_scanners(scanners_shifted_by, shift):
            if not shift in scanners_shifted_by.keys():
                scanners_shifted_by[shift] = move_all(
                        copy.deepcopy(scanners_shifted_by[shift - 1])
                    )

        for shift in count():
            solved = True
            maybe_create_new_scanners(scanners_shifted_by, shift)
            scanners = scanners_shifted_by[shift]

            last_shift = shift
            # Start the walk
            for position in range(max_depth + 1):
                cur_scanner = scanners[position]
                if cur_scanner.is_captured():
                    solved = False
                    break
                last_shift += 1
                maybe_create_new_scanners(scanners_shifted_by, last_shift)
                scanners = scanners_shifted_by[last_shift]

            if solved:
                return shift

# Test examples
assert solve('test.txt') == 10

# Solve riddle
print(solve('riddle.txt'))

