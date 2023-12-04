
import sys

def split_template(template):

    return [template[i:i+2] for i in range(len(template) - 1)]

def join_template(template):

    return template[0] + "".join([template[i][1] for i in range(1, len(template))])

def lookup(pattern, rules):

    for rule in rules:
        if rule["pattern"] == pattern:
            return rule["insert"]

def step(template, rules):

    new_template = []

    for el in template:

        insert = lookup(el, rules)

        new_template.append(el[0] + insert)
        new_template.append(insert + el[1])

    return new_template

def repeat_step(template, rules, steps):

    for i in range(steps):

        print("Step: {}".format(i))

        template = step(template, rules)
    
    return template

def sub(temp):

    count = {}

    for el in temp:
        if el in count: count[el] += 1
        else: count[el] = 1

    return count[max(count, key=count.get)] - count[min(count, key=count.get)]

def main():

    template = ""
    rules = []

    with open(sys.argv[1]) as f:

        lines = f.readlines()

        template = lines[0].strip()

        for i in range(2, len(lines)):

            rule = lines[i].split("->")

            rules.append({"pattern": rule[0].strip(), "insert": rule[1].strip()})

        temp = split_template(template)

        res = repeat_step(temp, rules, 20)

        print(sub(join_template(res)))

if __name__ == "__main__":
    main()