import pprint
import math

monkeys = {

}



def main():
  with open("input.txt", "r") as file:
    data = file.read().split("\n")
    current_monkey = 0
    for line in data:
      line = line.strip()
      if line.startswith("Monkey"):
        current_monkey = int(line.split(" ")[1].strip(":"))
        monkeys[current_monkey] = {}
      if line.startswith("Starting items:"):
        items = line.split(": ")[1].split(", ")
        monkeys[current_monkey]["items"] = list(map(int, items))
      if line.startswith("Operation:"):
        operation = line.split(": ")[1].split("= ")[1]
        monkeys[current_monkey]["operation"] = operation
      if line.startswith("Test:"):
        divider = line.split(" ")[-1]
        monkeys[current_monkey]["test"] = {}
        monkeys[current_monkey]["test"]["divider"] = int(divider)
      if line.startswith("If true:"):
        new_monkey = int(line.split(" ")[-1])
        monkeys[current_monkey]["test"]["true"] = new_monkey
      if line.startswith("If false:"):
        new_monkey = int(line.split(" ")[-1])
        monkeys[current_monkey]["test"]["false"] = new_monkey
  pprint.pprint(monkeys)
  items_handled = {}
  for i in range(len(monkeys.keys())):
    items_handled[i] = 0
  all_dividers = [v["test"]["divider"] for (k,v) in monkeys.items()]
  d = math.lcm(*all_dividers)
  print(all_dividers)
  for i in range(10000):

    for (monkey, values) in monkeys.items():
      items = [*values["items"]]
      for item in items:
        old = item
        new = 0
        new = eval(values["operation"])
        new = math.floor(new % d)
        if new % values["test"]["divider"] == 0:
          monkeys[values["test"]["true"]]["items"].append(new)
        else:
          monkeys[values["test"]["false"]]["items"].append(new)
        monkeys[monkey]["items"].pop(values["items"].index(item))
        items_handled[monkey] += 1

  print("")
  pprint.pprint(monkeys)
  handled = list(items_handled.values())
  handled.sort()
  print(handled[-1] * handled[-2])

if __name__ == "__main__":
  main()