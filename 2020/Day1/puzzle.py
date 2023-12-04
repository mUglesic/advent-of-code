def findSumOfTwo(lines, sum):
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i != j:
        if l1 + l2 == sum:
          return (l1, l2)

def findSumOfThree(lines, sum):
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      for k, l3 in enumerate(lines):
        if i != j and i != k and j != k:
          if l1 + l2 + l3 == sum:
            return (l1, l2, l3)

with open("input.txt", "r") as f:

  lines = f.readlines();

  for i, l in enumerate(lines):
    lines[i] = int(l)

  #a, b = findSumofTwo(lines, 2020)
  a, b, c = findSumOfThree(lines, 2020)

  print(a, " * ", b, " * ", c, " = ", a * b * c)

  f.close()