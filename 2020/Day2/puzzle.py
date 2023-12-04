def checkValidOld(text, char, mini, maxi):
  counter = 0
  for c in text:
    if c == char: counter += 1
  return (counter >= mini) and (counter <= maxi)

def checkValid(text, char, i, j):
  print("Text: %s, Search: %s, i = %d, j = %d; Result: %s" % (text, char, i, j, (text[i - 1] == char and text[j - 1] != char) or (text[i - 1] != char and text[j - 1] == char)))
  return (text[i - 1] == char and text[j - 1] != char) or (text[i - 1] != char and text[j - 1] == char)

def count(lines):
  counter = 0
  for i, line in enumerate(lines):
    l = line.split(":")
    condition = l[0].split(" ")
    minMax = condition[0].split("-")
    char = condition[1]
    #if checkValidOld(l[1].strip(), char, int(minMax[0]), int(minMax[1])): counter += 1
    if checkValid(l[1].strip(), char, int(minMax[0]), int(minMax[1])): counter += 1
  return counter

with open("input.txt", "r") as f:

  lines = f.readlines()

  res = count(lines)

  print(res)

  f.close()