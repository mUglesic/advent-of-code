
import sys

TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000

def allUnder(root, val, res):
    
    if (root.size() <= val):
        res.append(root)

    for el in root.contents:
        
        if isinstance(el, Dir):
            allUnder(el, val, res)

    return res

def allOver(root, val, res):
    
    if (root.size() >= val):
        res.append(root)

    for el in root.contents:
        
        if isinstance(el, Dir):
            allOver(el, val, res)

    return res

def solve(data):

    system = System('/')

    for i in range(len(data)):

        line = data[i]

        splitLine = line.split(' ')

        if splitLine[0] == '$':

            cmd = splitLine[1]

            match(cmd):
                case 'cd':
                    system.changeDir(splitLine[2])
                case 'ls':

                    j = i + 1
                    
                    while j < len(data):
                        
                        split = data[j].split(' ')
                        
                        if split[0] == '$': break

                        match (split[0]):
                            case 'dir':
                                system.add(Dir(split[1], system.current))
                            case _:
                                system.add(File(split[1], int(split[0])))

                        j += 1

        else:
            pass

    diff = NEEDED_SPACE - (TOTAL_SPACE - system.root.size())

    candidates = list(map(lambda x: x.size(), allOver(system.root, diff, [])))
    candidates.sort()

    return candidates[0]

    # return sum(map(lambda x: x.size(), allUnder(system.root, 100000, [])))

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)

class System:

    def __init__(self, root):
        self.root = Dir(root)
        self.current = self.root

    def changeDir(self, dir):
        if dir == '..':
            self.current = self.current.parent
        elif dir == '/':
            self.current = self.root
        else:
            # self.current.add(Dir(dir, self.current))
            self.current = self.current.findDir(dir)

    def add(self, element):
        self.current.add(element)

    def __str__(self):
        return f'{self.root}'

class Dir:

    def __init__(self, name, parent=None):
        self.name = name
        self.contents = []
        self.parent = self if (parent == None) else parent

    def add(self, element):
        self.contents.append(element)

    def findDir(self, dir):
        for el in self.contents:
            if el.name == dir:
                return el
        return self

    def size(self):
        s = 0
        for el in self.contents:
            s += el.size()
        return s

    def __str__(self):
        return self.name + '\n' + '\n'.join(map(lambda x: str(x), self.contents))

class File:

    def __init__(self, name, size):
        self.name = name
        self.s = size

    def size(self):
        return self.s

    def __str__(self):
        return f'{self.name} ({self.size})'


###########################

if __name__ == "__main__":
    main()
