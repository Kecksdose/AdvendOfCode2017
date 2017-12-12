def solve(file):
    with open(file, 'r') as f:
        programs = []
        program_names = set()
        for line in f.readlines():
            program = line.strip('\n')
            program = program.split()
            program_names.add(program[0])
            print(program)
        print(program_names)

# Test examples
solve('test.txt')
#assert solve('test.txt') == 42


# Solve riddle
#print(solve('riddle.txt'))

