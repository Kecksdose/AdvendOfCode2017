def check_condition(first, op, second):
    if op == '>':
        return first > second
    elif op == '<':
        return first < second
    elif op == '==':
        return first == second
    elif op == '!=':
        return first != second
    elif op == '>=':
        return first >= second
    elif op == '<=':
        return first <= second
    else:
        raise ValueError(f'Operation not known: {op}')

def apply(val, op, number):
    if op == 'inc':
        return val + number
    elif op == 'dec':
        return val - number
    else:
        raise ValueError(f'Operation not known: {op}')

def solve(file):
    with open(file, 'r') as f:
        all_vars = {}
        for line in f.readlines():
            line = line.strip('\n')
            line = line.split()

            # Example line
            # ['b', 'inc', '5', 'if', 'a', '>', '1']
            #   0     1     2     3    4    5    6  <-- indices

            # Initialise vars
            for index in [0, 4]:
                if not line[index] in all_vars.keys():
                    all_vars[line[index]] = 0

            # Check condition and apply operation
            if check_condition(
                first=all_vars[line[4]],
                op=line[5],
                second=int(line[6])
            ):
                all_vars[line[0]] = apply(
                    val=all_vars[line[0]],
                    op=line[1],
                    number=int(line[2]))

        return max(list(all_vars.values()))


# Test examples
assert solve('test.txt') == 1


# Solve riddle
print(solve('riddle.txt'))

