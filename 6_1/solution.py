### Example
# Four blocks:
# 0 2 7 0 (Chose 7)
# 2 4 1 2 (Chose 4)
# 3 1 2 3 (Chose first 3)
# 0 2 3 4 (Chose 4)
# 1 3 4 1 (Chose 4)
# 2 4 1 2
def solve(file):
    with open(file, 'r') as f:
        bank = f.read()
        bank = bank.strip('\n')
        bank = bank.split()
        bank = [int(val) for val in bank]

        n_blocks = len(bank)
        n_steps = 0
        # Memory
        has_been_seen = []
        has_been_seen.append(bank)

        while True:
            # Increase number of steps
            n_steps += 1

            # Get index of maximum
            new_bank = bank[:]

            max_index = 0
            max_val = 0
            for index in range(0, n_blocks):
                if new_bank[index] > max_val:
                    max_val = new_bank[index]
                    max_index = index

            # Spread blocks
            still_to_add = new_bank[max_index]
            new_bank[max_index] = 0
            cur_index = max_index

            for i in range(still_to_add):
                cur_index += 1
                if cur_index > n_blocks - 1:
                    cur_index = 0

                new_bank[cur_index] += 1

            # Test if it has been seen before
            if new_bank in has_been_seen:
                ### Only this line changed! ###
                return n_steps - has_been_seen.index(new_bank)

            # Add new bank to memory
            has_been_seen.append(new_bank)

            # Update bank
            bank = new_bank



# Test examples
assert solve('test.txt') == 4


# Solve riddle
print(solve('riddle.txt'))

