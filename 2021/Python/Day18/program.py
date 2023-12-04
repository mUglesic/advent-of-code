
import sys
import math
import ast

def parse_snail(line):

    l = ast.literal_eval(line)

    num = parse_rec(l)

    return num

def parse_rec(l):

    if isinstance(l, int):
        return l

    left = parse_rec(l[0])

    right = parse_rec(l[1])

    return Number(left, right)

def sum_snail(data):

    s = data[0]

    for i in range(1, len(data)):
        # print("\n{}\n+ {}\n".format(s, data[i]))
        s += data[i]
        # print("\n= {}\n".format(s))

    return s

def combo_snail(data):

    max_mag = 0

    for i in range(len(data)):
        for j in range(len(data)):
            
            el = data[i]
            other = data[j]

            if not el == other:
                
                # print(el, "\n+", other)
                s = el + other
                # print("=", s, "\n")
                max_mag = max(s.magnitude(s), max_mag)

            with open(sys.argv[1]) as f: data = [parse_snail(line.strip()) for line in f]
    
    return max_mag

def main():

    data = []

    with open(sys.argv[1]) as f:

        for line in f:

            data.append(parse_snail(line.strip()))

    # res = sum_snail(data)

    # print(res)

    # print(res.magnitude(res))

    res2 = combo_snail(data)

    print(res2)

    # test()

def test():

    n1 = Number(1, 1)
    n2 = Number(2, 2)
    n3 = Number(3, 3)
    n4 = Number(4, 4)
    n5 = Number(5, 5)
    n6 = Number(6, 6)

    nums = [n1, n2, n3, n4, n5, n6]

    print("\nValues: {}\n".format(", ".join(map(str, nums))))

    s = nums[0]

    for i in range(1, len(nums)): s += nums[i]

    print("Result: {}".format(s))

def test2():

    n1 = Number(Number(Number(Number(4, 3), 4), 4), Number(7, Number(Number(8, 4), 9)))
    n2 = Number(1, 1)

    s = n1 + n2

    print("\nResult: {}".format(s))

###########################################

class Number:

    def __init__(self, left, right):

        self.left = left
        self.right = right

        if isinstance(self.left, Number): self.left.parent = self
        if isinstance(self.right, Number): self.right.parent = self

        self.parent = None
        self.depth = 0

    def __add__(num1, num2):

        res = Number(num1, num2)

        if isinstance(num1, Number): num1.parent = res
        if isinstance(num2, Number): num2.parent = res

        if isinstance(num1, Number):
            num1.update_depth()
        if isinstance(num2, Number): 
            num2.update_depth()

        # print("after addition:\t{}".format(res))

        res.reduce()

        return res

    def magnitude(self, current):

        res = 0

        if isinstance(current, Number):
            res = 3 * self.magnitude(current.left)
            if isinstance(current.left, int): res += 3 * current.left
            if isinstance(current.right, int): res += 2 * current.right
            res += 2 * self.magnitude(current.right)

        return res

    def reduce(self):

        nested = self.find_depth(4)
        splittable = self.find_splittable()

        while nested or splittable:

            if (nested := self.find_depth(4)):
                nested.explode()
                # print("after explode:\t{}".format(self))
            elif (splittable := Number.find_splittable(self)):
                splittable[0].split()
                # print("after split:\t{}".format(self))

        pass

    def explode(self):

        left = self.find_left()
        right = self.find_right()

        if left:
            if self.is_parent(left):
                left.left += self.left
            else:
                left.right += self.left

        if right:
            if self.is_parent(right):
                right.right += self.right
            else: 
                right.left += self.right

        if self.parent.left == self:
            self.parent.left = 0
        elif self.parent.right == self:
            self.parent.right = 0

    def split(self):

        # print(self)

        if isinstance(self.left, int) and self.left >= 10:
            
            new_left = math.floor(self.left / 2)
            new_right = math.ceil(self.left / 2)

            num = Number(new_left, new_right)

            self.left = num
            num.parent = self

            num.update_depth()

            return

        if isinstance(self.right, int) and self.right >= 10:

            new_left = math.floor(self.right / 2)
            new_right = math.ceil(self.right / 2)

            num = Number(new_left, new_right)

            self.right = num
            num.parent = self

            num.update_depth()

            return

    def find_left(self):

        p = self.parent
        cur = self

        while p:

            if p.right == cur:
                
                if isinstance(p.left, int):
                    return p

                res = p.left

                while isinstance(res.right, Number):
                    res = res.right

                return res

            p = p.parent
            cur = cur.parent

        return None

    def find_right(self):

        p = self.parent
        cur = self

        while p:

            if p.left == cur:
                
                if isinstance(p.right, int):
                    return p

                res = p.right

                while isinstance(res.left, Number):
                    res = res.left

                return res

            p = p.parent
            cur = cur.parent

        return None

    def find_depth(self, d):

        if self.depth == d:
            return self

        left = None
        right = None

        if isinstance(self.left, Number):
            left = self.left.find_depth(d)

        if isinstance(self.right, Number):
            right = self.right.find_depth(d)

        return left if left else right

    def find_splittable(current):

        res = []

        if isinstance(current, Number):
            
            res = Number.find_splittable(current.left)
            res.append(current)
            res = res + Number.find_splittable(current.right)

        return Number.is_splittable(res)

    def is_parent(self, other):

        p = self.parent

        while p:

            if p == other:
                return True

            p = p.parent

        return False

    def is_splittable(arr):

        new_arr = []

        for el in arr:
            if isinstance(el, Number):
                if (isinstance(el.left, int) and el.left >= 10) or (isinstance(el.right, int) and el.right >= 10):
                    new_arr.append(el)
        
        return new_arr

    def update_depth(self):

        p = self.parent
        d = 0

        while p:
            d += 1
            p = p.parent
        
        self.depth = d

        if isinstance(self.left, Number):
            self.left.update_depth()

        if isinstance(self.right, Number):
            self.right.update_depth()

    def __str__(self):
        return "[{},{}]".format(self.left, self.right)

    def __repr__(self):
        return "Value: {}\nParent: {}\nDepth: {}\n".format(self, self.parent, self.depth)

if __name__ == "__main__":
    main()