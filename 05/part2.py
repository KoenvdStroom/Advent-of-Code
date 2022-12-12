import math
import re
def main():
  stacks = []
  with open("input.txt", "r") as f:
    inp = f.read().split("move")
    original_stacks = inp[0].split("\n")
    total_rows = int((len(original_stacks[0])+1)/4)
    for i in range(total_rows):
      stacks.append([])
    for line in original_stacks:
      prev_row = 0
      spaces = 0
      count_next = False
      for char in line:
        if count_next:
          row = math.ceil(max(0, spaces)/4)+prev_row
          stacks[row].append(char)
          spaces = 0
          count_next = False
          prev_row = row
        if(char == " "):
          spaces +=1
        elif char == "[":
          count_next = True
    for i in stacks:
      i.reverse()
    moves = inp[1:]
    for move in moves:
      move = move.strip("\n").strip()
      regex = "([0-9]+) from ([0-9]+) to ([0-9]+)"
      matches = re.findall(regex, move)[0]
      amount = int(matches[0])
      from_row = int(matches[1])
      to_row = int(matches[2])
      for i in range(amount, 0, -1):
        print("From:",from_row-1, stacks[from_row-1])
        print("To:",to_row-1,  stacks[to_row-1])
        print("Item:", -i)
        stacks[to_row-1].append(stacks[from_row-1][-i])
        stacks[from_row-1].pop(-i)
  code = ""
  for i in stacks:
    print(i)
    code += i[-1]
  print(code)
  



if __name__ == "__main__":
  main()