from collections import namedtuple


class File:

    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def file(self, name):
        for file in self.files:
            if file.name == name:
                return file

    def total_size(self):
        size = self.size
        for file in self.files:
            size += file.total_size()
        return size


Command = namedtuple('Command', ['command', 'output'])


def parse_input():
    f = open('day07/input.txt')
    #f = open('day07/example.txt')
    lines = f.readlines()
    f.close()

    commands = []
    command = None
    output = []
    for line in lines:
        line = line.replace('\n', '')
        if line.startswith('$'):
            if command is not None:
                commands.append(Command(command, output))
                output = []
                command = None
            command = line[2:]
        else:
            output.append(line)

    return commands[1:]


def parse_commands(commands):
    root = File("/")
    currentDir = root
    for command in commands:
        if command.command.startswith('ls'):
            for line in command.output:
                if (line.startswith('dir')):
                    currentDir.add_file(File(line[4:], parent=currentDir))
                else:
                    parts = line.split()
                    currentDir.add_file(File(parts[1], int(parts[0]), currentDir))
        else:
            if command.command.endswith('..'):
                currentDir = currentDir.parent
            else:
                dest = command.command.split()[1]
                currentDir = currentDir.file(dest)

    return root


def sum_sizes(dir):
    dirsize = dir.total_size()
    size = 0
    if dirsize < 100000 and dir.size == 0:
        size += dirsize

    for file in dir.files:
        size += sum_sizes(file)

    return size


def part_a(tree):
    size = sum_sizes(tree)
    
    print(f'[a] size of directories <= 100000 = {size}')


def get_min_dir(dir, needed):
    min_size = dir.total_size()
    min_dir = dir

    for file in dir.files:
        child_min_size, child_min_dir = get_min_dir(file, needed)
        if child_min_size <= min_size and child_min_size > needed:
            min_dir = child_min_dir
            min_size = child_min_size

    return min_size, min_dir


def part_b(tree):

    needed = 30000000 - (70000000 - tree.total_size())
    min_size, min_dir = get_min_dir(tree, needed)

    print(f'[b] smallest dir to delete = {min_dir.name}, size={min_size}')


def main():
    commands = parse_input()
    tree = parse_commands(commands)

    part_a(tree)

    part_b(tree)


if __name__ == '__main__':
    main()
