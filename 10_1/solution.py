from functools import reduce

def solve(file, list_size=256):
    with open(file, 'r') as f:
        lengths = f.read()
        lengths = lengths.strip('\n')
        lengths = [ord(char) for char in lengths]

        # Special case: empty string as input

        # Add standard length suffix values
        lengths += [17, 31, 73, 47, 23]

        # Create base list and calculate sparse hash
        base_list = list(range(0, 256))

        skip_size = 0
        cur_index = 0

        for _ in range(0, 64):
            for i, length in enumerate(lengths, start=1):
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

        # Calculate dense hash
        base_list = [
            reduce(
                lambda x, y: x^y, base_list[i*16:((i*16)+16)]
            ) for i in range(16)
        ]

        # Convert to hex and return
        hash_list = []

        for val in base_list:
            hex_val = hex(val)
            if len(hex_val) == 4:
                hash_list.append(hex_val[2:])
            elif len(hex_val) == 3:
                hash_list.append('0' + hex_val[-1])
            else:
                raise ValueError(f'Hex val of {val} not understood.')

        return ''.join(hash_list)


# Test examples
files_and_solutions = {
    'test1.txt': 'a2582a3a0e66e6e86e3812dcb672a272',
    'test2.txt': '33efeb34ea91902bb2f59c9920caa6cd',
    'test3.txt': '3efbe78a8d82f29979031a4aa0b16a9d',
    'test4.txt': '63960835bcdc130f0b66d7ff4f6a5a8e'
}

for file, solution in files_and_solutions.items():
    assert solve(file) == solution


# Solve riddle
print(solve('riddle.txt'))
