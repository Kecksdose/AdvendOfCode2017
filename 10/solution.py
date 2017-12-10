def solve(file, list_size=256):
    with open(file, 'r') as f:
        lengths = f.read()
        lengths = lengths.strip('\n')
        lengths = lengths.split(',')
        lengths = [int(length) for length in lengths]
        base_list = list(range(0, list_size))

        skip_size = 0
        cur_index = 0

        for length in lengths:
            # Get sub_list
            remaining = length + cur_index - list_size

            # Remaining should be in 0..list_size - 1
            # TODO: Tidy this up a bit
            if remaining > list_size:
                remaining % list_size

            if remaining < 0:
                sub_list = base_list[cur_index:cur_index+length]
            else:
                sub_list = base_list[cur_index:]
                sub_list += base_list[0:remaining]

            # Invert sub_list
            sub_list = sub_list[::-1]

            # Insert
            if remaining < 0:
                base_list[cur_index:cur_index+length] = sub_list
            else:
                base_list[cur_index:] = sub_list[0:len(sub_list)-remaining]
                base_list[0:remaining] = sub_list[len(sub_list)-remaining:]

            # Walk
            cur_index  = cur_index + length + skip_size
            cur_index = cur_index % list_size

            # Increment skip_size
            skip_size += 1

        return base_list[0] * base_list[1]


# Test examples
assert solve('test.txt', list_size=5) == 12


# Solve riddle
print(solve('riddle.txt'))
