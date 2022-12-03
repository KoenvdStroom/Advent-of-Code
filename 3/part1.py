alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
  total_prio = []
  with open("input.txt", "r") as f:
    data = f.readlines()
    for rucksack in data:
      length_of_comp = len(rucksack)//2
      comp_one = rucksack[:length_of_comp]
      comp_two = (rucksack[length_of_comp:]).strip("\n")
      for i in comp_one:
        if i in comp_two:
          prio = alphabet.find(i) + 1
          total_prio.append(prio)
          break

  print(sum(total_prio))


if __name__ == "__main__":
  main()