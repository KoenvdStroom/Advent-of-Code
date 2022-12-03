alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
  total_prio = []
  rows = []
  with open("input.txt", "r") as f:
    data = f.readlines()
    i = 0
    current = []
    for rucksack in data:
      current.append(rucksack)
      i+=1
      if i==3:
        rows.append(current)
        current = []
        i = 0
  for group in rows:
      rucksack_one = group[0]
      rucksack_two = group[1]
      rucksack_three = group[2]
      for i in rucksack_one:
        if i in rucksack_two and i in rucksack_three:
          total_prio.append(alphabet.find(i) + 1)
          break
  print(sum(total_prio))


if __name__ == "__main__":
  main()